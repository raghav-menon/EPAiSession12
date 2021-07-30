# Polygon.py
import math


class Polygon:
    """Implementation of a regular Polygon which takes num_eges and \
        circumradius as input. It can give num_eges, num_vertices,interior \
            angle,edge length,apothem,area,perimeter \
            """
    def __init__(self, count_edges: int = 3, circumradius : float = 1.0) -> None:
        """ Function to initialize the num of edges and circumradius"""
        
        if count_edges < 3:
            raise ValueError("Polygon must have atleast 3 edges")
        self._count_edges = count_edges
        self._circumradius = circumradius
        self._interior_angle = None
        self._apothem = None
        self._side_length = None
        self._area = None
        self._perimeter = None

    @property
    def count_edges(self):
        """ Function to return the number of edges"""
        return self._count_edges
    
    @count_edges.setter
    def count_edges(self, value):
        """Function to set the number of vertices"""
        if(value < 3):
            raise ValueError(" Radius should be greater than 3")
        self._count_edges = value
        self._interior_angle = None
        self._apothem = None
        self._side_length = None
        self._area = None
        self._perimeter = None

    @property
    def count_vertices(self):
        """ Function to return the number of vertices. Number of vertices \
            equals number of edges in a regular polygon"""
        return self._count_edges
    
    @count_vertices.setter
    def count_vertices(self, value):
        """Function to set the number of vertices"""
        if(value < 3):
            raise ValueError(" Radius should be greater than 3")
        self._count_edges = value
        self._interior_angle = None
        self._apothem = None
        self._side_length = None
        self._area = None
        self._perimeter = None

    @property
    def circumradius(self):
        """ Function to return Circumradius"""

        return self._circumradius

    @circumradius.setter
    def circumradius(self, value):
        """ Setter for Circumradius"""
        if(value < 0):
            raise ValueError(" Radius should be greater than 0")
        self._circumradius = value
        self._interior_angle = None
        self._apothem = None
        self._side_length = None
        self._area = None
        self._perimeter = None

    @property
    def interior_angle(self):
        """Function to calculate the interior angle"""
        if self._interior_angle is None:
            self._interior_angle = (self.count_edges - 2) * 180 / self.count_edges
        return self._interior_angle

    @property
    def side_length(self):
        """Function to calculate the edge length"""
        if self._side_length is None:
            self._side_length = 2 * self.circumradius * math.sin(math.pi / self.count_edges)
        return self._side_length

    @property
    def apothem(self):
        """Function to calculate the apothem"""
        if self._apothem is None:
            self._apothem = self.circumradius * math.cos(math.pi / self.count_edges)
        return self._apothem

    @property
    def area(self):
        """Function to calculate the area"""
        if self._area is None:
            self._area = 1/2 * self.count_edges * self.side_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        """Function to calculate the perimeter"""
        if self._perimeter is None:
            self._perimeter = self.count_edges * self.side_length
        return self._perimeter

    def __repr__(self):
        """Repr Function to return the no of edges and Circumradius"""
        return f"Polygon(n={self.count_vertices}, R={self.circumradius})"

    def __eq__(self, other):
        """Equality function to compare whether 2 polygons are equal by \
            comparing the number of edges and circumradius"""
        if isinstance(other, self.__class__):
            return self.count_edges == other.count_edges and self.circumradius == other.circumradius
        else:
            return NotImplemented

    def __gt__(self, other):
        """Greater than function to compare whether which of the 2 polygons \
            is bigger by comparing the number of vertices"""
        if isinstance(other, self.__class__):
            return self.count_edges > other.count_edges
        else:
            return NotImplemented
