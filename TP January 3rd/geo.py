#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Rectangle:
    n_edges=4
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def rectangle_area(self):
        return self.length*self.width
    
    def rectangle_perimeter(self):
        return 2*self.length + 2*self.width
    
    @staticmethod
    def talk():
        return "Do you like rectangles?"

class Patch:
    n_edges=4
    
    def __init__(self,rectangle):
        self.length = 1
        self.abs_max=rectangle.width
        self.ord_max=rectangle.length
    
    
    def __iter__(self):
        self.absi=1
        self.ordi=1
        return self
    
    def __next__(self):
        
        
        if self.absi+1<=self.abs_max:
            self.absi+=1
        elif self.absi+1>self.abs_max:
            self.absi=1
            if self.ordi+1<=self.ord_max:
                self.ordi+=1
            elif self.ordi+1>self.ord_max:
                raise StopIteration
        return(self.absi-1,self.ordi-1)

