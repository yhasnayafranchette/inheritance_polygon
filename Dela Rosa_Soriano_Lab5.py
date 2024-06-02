# Laboratory Activity 5: DELA ROSA, SORIANO
# Polygon Hierarchy

class Polygon:
    def __init__(self, type, sides, vertices, diagonals, side_lengths):
        self.type = type
        self.sides = sides
        self.vertices = vertices
        self.diagonals = diagonals
        self.side_lengths = side_lengths

    def calculate_perimeter(self):
        perimeter = sum(self.side_lengths)
        return perimeter
    
    def display_polygon_info(self):
        info = f"Type of Polygon: {self.type}\n"
        info += f"Number of Sides: {self.sides}\n"
        info += f"Number of Vertices: {self.vertices}\n"
        info += f"Number of Diagonals: {self.diagonals}\n"
        return info
    
    def display_info_with_perimeter(self):
        info = self.display_polygon_info()
        info += f"Side Lengths: {self.side_lengths}\n"
        info += f"Perimeter: {self.calculate_perimeter()}"  
        return info
            
# Polygon that has Three(3) sides 
class Triangle(Polygon):
    def __init__(self, type, vertices, diagonals, side_lengths, angles):
        super().__init__(type, 3, vertices, diagonals,side_lengths)
        self.angles = angles

    def calculate_sum_of_interior_angles(self): 
        interior = (self.sides - 2) * 180
        return interior
    
    def triangle_based_on_sides_info(self):
        return super().display_info_with_perimeter()
    
    def triangle_based_on_angles_info(self):
        info = super().display_polygon_info()  
        info += f"Angles: {self.angles[0]}°, {self.angles[1]}°, {self.angles[2]}°\n"
        info += f"Sum of Interior Angles: {self.calculate_sum_of_interior_angles()}°\n"
        return info

# Triangle Based on Sides: Equilateral - three sides have the same length
class Equilateral(Triangle):
    def __init__(self, type, vertices, diagonals, side_length, angles):
        super().__init__(type, vertices, diagonals, [side_length, side_length, side_length], angles)

    def check_equilateral(self):
        if self.side_lengths[0] == self.side_lengths[1] == self.side_lengths[2]:
            return "Equilateral Triangle"
        else:
            return "This polygon may be another type of triangle based on sides"

    def display_equilateral_info(self):
        info = f"{self.check_equilateral()}\n"
        info += f"{super().triangle_based_on_sides_info()}\n"
        return info

# Triangle Based on Sides: Scalene - all three sides are in different lengths
class Scalene(Triangle):
    def __init__(self, type, vertices, diagonals, side_lengths, angles):
        super().__init__(type, vertices, diagonals, side_lengths, angles)

    def check_scalene(self):
        if self.side_lengths[0] != self.side_lengths[1] != self.side_lengths[2]:
            return "Scalene Triangle"
        else:
            return "This polygon may be another type of triangle based on sides"
        
    def display_scalene_info(self):
        info = f"{self.check_scalene()}\n"
        info += f"{super().triangle_based_on_sides_info()}\n"
        return info
    
# Triangle Based on Sides : Isosceles - has two sides of equal length
class IsoscelesTriangle(Triangle):
    def __init__(self, type, vertices, diagonals, side_lengths, angles):
        super().__init__(type, vertices, diagonals, side_lengths, angles)

    def check_isosceles(self):
        if self.side_lengths[0] == self.side_lengths[1] or self.side_lengths[1] == self.side_lengths[2] or self.side_lengths[0] == self.side_lengths[2]:
            return "Isosceles Triangle"
        else:
            return "This polygon may be another type of triangle based on sides"
        
    def display_isosceles_triangle_info(self):
        info = f"{self.check_isosceles()}\n"
        info += f"{super().triangle_based_on_sides_info()}\n"
        return info

# Triangle Based on Angles: Right -  one angle equal to 90° and the other two are acute angles  
class Right(Triangle):
    def __init__(self, type, vertices, diagonals, side_lengths, angles):
        super().__init__(type, vertices, diagonals, side_lengths, angles)

    def check_right(self):
        if self.angles.count(90) == 1:
            return "Right Triangle"
        else:
            return "This polygon may be another type of triangle based on angles"
        
    def display_right_info(self):
        info = f"{self.check_right()}\n"
        info += f"{super().triangle_based_on_angles_info()}"
        return info

# Triangle Based on Angles: Obtuse - an angle which is greater than 90° and less than 180° 
class Obtuse(Triangle):
    def __init__(self, type, vertices, diagonals, side_lengths, angles):
        super().__init__(type, vertices, diagonals, side_lengths, angles)

    def check_obtuse(self):
        if max(self.angles) > 90:
            return "Obtuse Triangle"
        else:
            return "This polygon may be another type of triangle based on angles"
        
    def display_obtuse_info(self):
        info = f"{self.check_obtuse()}\n"
        info += f"{super().triangle_based_on_angles_info()}"
        return info

# Triangle Based on Angles: Acute - all three interior angles are less than 90°      
class Acute(Triangle):
    def __init__(self, type, vertices, diagonals, side_lengths, angles):
        super().__init__(type, vertices, diagonals, side_lengths, angles)

    def check_acute(self):
        if all(angle < 90 for angle in self.angles):
            return "Acute Triangle"
        else:
            return "This polygon may be another type of triangle based on angles"
        
    def display_acute_info(self):
        info = f"{self.check_acute()}\n"
        info += f"{super().triangle_based_on_angles_info()}"
        return info

# Polygon that has Four(4) sides 
class Quadrilateral(Polygon):
    def __init__(self, type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides):
        super().__init__(type, 4, vertices, diagonals, side_lengths)
        self.parallel_sides = parallel_sides
        self.pair_parallel_sides = pair_parallel_sides
        self.top_side = side_lengths[0]
        self.bottom_side = side_lengths[1]
        self.left_side = side_lengths[2]
        self.right_side = side_lengths[3]

    def display_quadrilateral_info(self):
        info = f"{super().display_info_with_perimeter()}\n"
        info += f"Number of Parallel Sides: {self.parallel_sides}\n"
        info += f"Number of Pair Parallel Sides: {self.pair_parallel_sides}\n"
        return info

# Quadrilateral with Two Parallel Sides 
class Trapezoid(Quadrilateral): 
    def __init__(self, type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides):
        super().__init__(type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides)

    def check_trapezoid(self):
        if self.parallel_sides == 2: 
            return "Trapezoid"
        else:
            return "This polygon may be another type of quadrilateral."

    def display_trapezoid_info(self):
        info = f"{self.check_trapezoid()}\n"
        info += f"{super().display_quadrilateral_info()}"
        return info

# Quadrilateral with Two Parallel Sides and a Type of Trapezoid 
class IsoscelesTrapezoid(Trapezoid):
    def __init__(self, type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides):
        super().__init__(type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides)

    def check_isosceles_trapezoid(self):
            if self.parallel_sides == 2 and self.left_side == self.right_side: 
                return "Isosceles Trapezoid"
            else:
                return "This polygon is not an Isosceles Trapezoid"

    def display_isosceles_trapezoid_info(self):
        info = f"{self.check_isosceles_trapezoid()}\n"
        info += f"{super().display_quadrilateral_info()}"
        return info

# Quadrilateral with Two Pairs of Parallel Sides 
class Parallelogram(Quadrilateral):
    def __init__(self, type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides):
        super().__init__(type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides)

    def check_parallelogram(self):
        if self.pair_parallel_sides == 2 and self.parallel_sides == 4:
            return "Parallelogram"
        else:
            return "This polygon is not a Parallelogram."

    def display_parallelogram_info(self):
        info = f"{self.check_parallelogram()}\n"
        info += f"{super().display_quadrilateral_info()}"
        return info

# Quadrilateral with Two Pairs of Parallel Sides and a Type of Parallelogram: Rectangle - opposite sides of the rectangle are equal in length 
class Rectangle(Parallelogram):
    def __init__(self, type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides):
        super().__init__(type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides)

    def check_rectangle(self):
        if self.top_side == self.bottom_side and self.left_side == self.right_side:
            return "Rectangle"
        else:
            return "This polygon is not a Rectangle."

    def display_rectangle_info(self):
        info = f"{self.check_rectangle()}\n"
        parallelogram_info = super().display_parallelogram_info().replace("Parallelogram", "").strip()
        info += parallelogram_info
        return info + "\n"

# Quadrilateral with Two Pairs of Parallel Sides and a Type of Parallelogram: Rhombus -  four sides all have the same length
class Rhombus(Parallelogram):
    def __init__(self, type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides):
        super().__init__(type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides)

    def check_rhombus(self):
        if self.top_side == self.bottom_side == self.right_side == self.left_side:
            return "Rhombus"
        else:
            return "This polygon is not a Rhombus."

    def display_rhombus_info(self):
        info = f"{self.check_rhombus()}\n"
        parallelogram_info = super().display_parallelogram_info()
        parallelogram_info = parallelogram_info.replace("Parallelogram", "").strip()
        info += parallelogram_info
        return info + "\n"

# Quadrilateral with Two Pairs of Parallel Sides and Share all the Properties of Both Rectangle and Rhombus
class Square(Rectangle, Rhombus): 
    def __init__(self, type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides):
        super().__init__(type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides)

    def check_square(self):
        if super().check_rectangle() == "Rectangle" and super().check_rhombus() == "Rhombus":
            return "Square"
        else:
            return "This polygon is not a square and a type of rectangle and rhombus"

    def display_square_info(self):
        info = f"{self.check_square()}\n"
        square_info = f"{super().display_rectangle_info()}\n"
        square_info = square_info.replace("Rectangle", "").replace("Rhombus", "").replace("Parallelogram", "")
        info += square_info.strip()
        return info + "\n"
    
# Quadrilateral with No Parallel Sides
class Kite(Quadrilateral):
    def __init__(self, type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides):
        super().__init__(type, vertices, diagonals, side_lengths, parallel_sides, pair_parallel_sides)

    def check_kite(self): 
        if self.parallel_sides == 0: 
            return "Kite"
        else:
            return "This polygon is not a Kite."
        
    def display_kite_info(self):
        info = f"{self.check_kite()}\n"
        info += f"{super().display_quadrilateral_info()}"
        return info    

# Polygon that has Five(5) sides
class Pentagon(Polygon):
    def __init__(self, type, vertices, diagonals, side_lengths):
        super().__init__(type, 5, vertices, diagonals,side_lengths)
    
    def check_pentagon(self):
        if self.sides == 5: 
            return "Polygon with 5 sides"
        else:
            return "This polygon is not pentagon."
        
    def display_pentagon_info(self):
        info = f"{self.check_pentagon()}\n"
        info += f"{super().display_info_with_perimeter()}\n"
        return info

# Polygon that has Six(6) sides
class Hexagon(Polygon):
    def __init__(self, type, vertices, diagonals, side_lengths):
        super().__init__(type, 6, vertices, diagonals, side_lengths)
    
    def check_hexagon(self):
        if self.sides == 6: 
            return "Polygon with 6 sides"
        else:
            return "This polygon is not hexagon."
        
    def display_hexagon_info(self):
        info = f"{self.check_hexagon()}\n"
        info += f"{super().display_info_with_perimeter()}\n"
        return info
    
equilateral_triangle = Equilateral("Triangle", 3, 0, 5, None)
print(equilateral_triangle.display_equilateral_info())
        
scalene_triangle = Scalene("Triangle", 3, 0, [5, 6, 7],None)
print(scalene_triangle.display_scalene_info())

isosceles_triangle = IsoscelesTriangle("Triangle", 3, 0, [5, 5, 7],None)
print(isosceles_triangle.display_isosceles_triangle_info())

right_triangle = Right("Triangle", 3, 0, None, [90, 45, 45])
print(right_triangle.display_right_info())

obtuse_triangle = Obtuse("Triangle", 3, 0, None, [110, 30, 40])
print(obtuse_triangle.display_obtuse_info())

acute_triangle = Acute("Triangle", 3, 0, None, [60, 60, 60])
print(acute_triangle.display_acute_info())

trapezoid = Trapezoid("Quadrilateral", 4, 2,[8, 5, 3, 6], 2, 1)
print(trapezoid.display_trapezoid_info())

isosceles_trapezoid = IsoscelesTrapezoid("Quadrilateral", 4, 2, [6,7,5,5], 2, 1)
print(isosceles_trapezoid.display_isosceles_trapezoid_info())

parallelogram = Parallelogram("Quadrilateral", 4, 2, [10,10, 8, 8], 4, 2)
print(parallelogram.display_parallelogram_info())

rectangle = Rectangle("Quadrilateral", 4, 2, [2, 2, 3, 3], 4, 2)
print(rectangle.display_rectangle_info())

rhombus = Rhombus("Quadrilateral", 4, 2, [8,8,8,8], 4, 2)
print(rhombus.display_rhombus_info())

square = Square("Quadrilateral", 4, 2, [2, 2, 2, 2], 4, 2)
print(square.display_square_info())

kite = Kite("Quadrilateral", 4, 2, [8,6,8,6], 0, 0)
print(kite.display_kite_info())

pentagon = Pentagon("Pentagon", 5, 5, [5, 5, 5, 5, 5])
print(pentagon.display_pentagon_info())

hexagon = Hexagon("Hexagon", 6, 9, [6, 6, 6, 6, 6, 6])
print(hexagon.display_hexagon_info())