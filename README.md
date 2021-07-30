## Session 12 - Iterators and Iterables II

## Lazy Evaluation

Lazy Evaluation is a strategy which delays the evaluation of an expression until its value is needed and which also avoids repeated evaluations. 
This is usually done to optimize the code. Thus lazy evaluation does not evaluate the code immediately but only when it is needed. It is also called
call-by-need.

## Assignment

The starting point for this assignment is the `Polygon` class and the `Polygons` sequence type you created in the previous assignment.

The code for these classes along with the unit tests for the `Polygon` class are below if you want to use those as your starting point. But use whatever 
you came up with in the last project.

You have two goals:

###Goal 1:

Refactor the `Polygon` class so that all the calculated properties are lazy properties, i.e. they should still be calculated properties, 
but they should not have to get recalculated more than once (since we made our `Polygon` class "immutable").
 
###Goal 2:

Refactor the `Polygons` (sequence) type, into an **iterable**. Make sure also that the elements in the iterator are computed lazily - i.e. you can no 
longer use a list as an underlying storage mechanism for your polygons.

You'll need to implement both an iterable and an iterator.


## Class Polygon 

Implementation of a regular Polygon which takes num_eges and circumradius as input. It can give num_eges, num_vertices,interior angle, edge length,
apothem, area, perimeter

**Usage**

```python
p = Polygon(10, 10) # no of edges , circumradius
p.num_edges
p.perimeter
p.area

```

### __init__ 
This function initializes the number of edges and the circumradius to the polygon class. All the properties i.e. the interior_angle, area, apothem, perimeter
and side length are set to None in order to introduce lazy evaluation.

### count_edges
This function returns the number of edges. This is decorated as class property. Also decorated with count_edges.setter, it helps to set the edges values.Each time
the setter is called, all the properties are set to None as it would require re-evaluation

## count_vertices
This function returns the number of edges. This is decorated as class property. Also decorated with count_vertices.setter, it helps to set the edges values.
For a regular polygon, the number of edges is equal to the number of vertices. Each time the setter is called, all the properties are set to None as it would 
require re-evaluation.

## circumradius
This function returns the circumradius. This is decorated as class property. Also decorated with circumradius.setter, it helps to set the circumradius
value. Each time the circumradius's setter is called, all the properties are set to None as it would require re-evaluation.

## interior_angle
This function calculates the interior angle in accordance to the equation. This is decorated as class property. The interior angle is only calculated when it 
is called and only if its value is None making it a lazy evaluation. Thus subsequent calls to the interior angle with the same values of edge and circumradius
causes the return of the evaluated result.

## side_length
This function calculates the edge length in accordance to the equation. This is decorated as class property. The side length is only calculated when it 
is called and only if its value is None making it a lazy evaluation. Thus subsequent calls to the side length with the same values of edge and circumradius
causes the return of the evaluated result.

## apothem
This function calculates the apothem in accordance to the equation. This is decorated as class property. The apothem is only calculated when it 
is called and only if its value is None making it a lazy evaluation. Thus subsequent calls to the apothem with the same values of edge and circumradius
causes the return of the evaluated result.

## area
This function calculates the area in accordance to the equation. This is decorated as class property. The area is only calculated when it 
is called and only if its value is None making it a lazy evaluation. Thus subsequent calls to the area with the same values of edge and circumradius
causes the return of the evaluated result.

## perimeter
This function calculates the perimeter in accordance to the equation. This is decorated as class property. The perimeter is only calculated when it 
is called and only if its value is None making it a lazy evaluation. Thus subsequent calls to the perimeter with the same values of edge and circumradius
causes the return of the evaluated result.

## __repr__
This function returns the property of the Polygon class initialized

## __eq__
Equality function to compare whether 2 polygons are equal by comparing the number of edges and circumradius

## __gt__
Greater than function to compare whether which of the 2 polygons is bigger by comparing the number of vertices


## Class Polygons
Implementaion Of Custom Sequence of Polygons which takes largest polygon num of edges and circumradius as input

**Usage**

```python
p = Polygons(num_edges = 10,  circumradius = 10) 

#for getting the each Polygon through index
p[3]

#slicing
p[3:10]

#length
len(p)

#max efficinecy polygon
p.max_efficiency_polygon


```

## __init__ 
This function initializes the largest number of edges and the circumradius to the polygon sequence class. The polygon sequence class generates a sequence of 
polygons greater than 2 upto the polygon with the largest number of edges. Maximum efficiency (_max_eff) is set to None for lazy evaluation. It can be seen that
the polygons in the sequence are not calculated and stored in a variable of type list.

## __len__
This function returns the length of the sequence. 

## max_edges
This function returns the maximum number of edges. This is decorated as class property. Also decorated with max_edges.setter, it helps to set the maximum
edges value. The maximum efficiency is set to None so as to recalculate lazily.

## circumradius
This function returns the circumradius. This is decorated as class property. Also decorated with circumradius.setter, it helps to set the circumradius
value. The maximum efficiency is set to None so as to recalculate lazily.

## __repr__
This function returns the property of the Polygon sequence class initialized.

## __getitem__
This function helps to retrieve a particular value from the polygon sequence or a slice of values. The value to be returned, be it a single element of the list
or a sequence of elements [slice of the sequence] as a list is calculated and returned only when required or that particular element or slice has to be retrieved.

## __iter__
This function returns the PolygonIter class which is an class inside the Polygons. This function makes the Polygon sequence class an iterator.

## __reversed__
This function is implemented to reverse the sequence in the descending order of edges. 

## _polygon
Calls the polygon class to get the properties

## max_efficiency_polygon
Calculates the maximum efficiency polygon

## PolygonIter Class
Class implemeted to obtain the next element of the polygon sequence


The deepnote link to this is https://deepnote.com/project/Lazy-Evaluations-kzFqUnQUSmurp0utPU-h5Q/%2FPolygon_LazyIterator.ipynb
