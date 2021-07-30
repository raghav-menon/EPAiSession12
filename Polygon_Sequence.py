from Polygon import Polygon

class Polygons:
    """Implementaion Of Custom Sequence of Polygons which takes largest \
        polygon num of edges and circumradius as input"""

    def __init__(self, m, R):
        """ Function initialising the number of edges and circumradius"""
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._max_eff = None
    
    @property
    def max_edges(self):
        """ Function to return the number of edges"""
        return self._m
    
    @max_edges.setter
    def max_edges(self, value):
        self._m = value
        self._max_eff = None
    
    @property
    def circumradius(self):
        """ Function to return the number of edges"""
        return self._R
    
    @circumradius.setter
    def circumradius(self, value):
        self._R = value
        self._max_eff = None

    def __len__(self):
        """Function returning the length of sequence"""
        return self._m - 2
    
    def __getitem__(self, pos):
        """Function to retrieve a particular element in the sequence or a \
            list of elements"""
        print("Inside __getitem__")
        if isinstance(pos, int):
            if pos < 0:
                pos = self._m - 2 + pos
            if pos < 0 or pos >= (self._m - 2):
                raise IndexError
            else:
                return self._polygon(pos + 3)
        else:
            start, stop, step = pos.indices(self._m-2)
            rng = range(start, stop, step)
            return [self._polygon(i+3) for i in rng]

    def __repr__(self):
        """Repr Function to print regarding the initialized variables"""
        return f'Polygons(m={self._m}, R={self._R})'

    def __iter__(self):
        """Iterator Function--> This function converts this class to an \
            Iterator returning an Iterator object"""
        return self.PolygonIter(self, self.__len__)
    
    def _polygon(self, num_edges):
        """Function returning a polygon of particular num of edges and \
            circumradius along with all the properties"""
        return Polygon(num_edges, self._R)

    @property
    def max_efficiency_polygon(self):
        """Function returning the max efficiency calculated according to the \
            formulae"""
        if self._max_eff is None:
            print(self)
            self._max_eff = sorted(self, key=lambda polygon: polygon.area/polygon.perimeter)[-1]        
        return self._max_eff
    
    def __reversed__(self):
        return self.PolygonIter(self, self.__len__, reverse=True)

    class PolygonIter:
        """This is an Iterator class which converts the main class into an \
            Iterator"""

        def __init__(self, polyobj, length, reverse=False):
            """Function initializing the polygon sequence object and \
                index. Index is used to return the next element in the polygon\
                    sequence when used as a iterator"""
            self._polyobj = polyobj
            self.reverse = reverse
            self._length = length
            self._index = 0

        def __iter__(self):
            """Iterator function which makes it an iterator object"""
            return self

        def __next__(self):
            """Next function to return the next element from an polygon \
                sequence iterator object"""
            if self._index >= len(self._polyobj):
                raise StopIteration
            else:
                if self.reverse:
                    index = len(self._polyobj) - 1 - self._index
                else:
                    index = self._index
                item = self._polyobj._polygon(index+3)
                self._index += 1
                return item
