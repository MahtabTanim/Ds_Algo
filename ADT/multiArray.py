class MultiArray :
    def __init__(self,*dims) :
        assert len(dims)>1 , "Number of dimeonsion must be 2 or More"
        self._dims = len(dims)
        self._dimArray = list(dims)
        size = 1
        for d in dims:
            assert d>0,"Dimeonsion must be > 0"
            size*= d
        self._elements = [None]*size
        self._factors = [None]* len(dims)
        self._computefactors(dims)
    def numDims(self):
        return self._dims
    def length(self,dim):
        assert dim>=1 and dim<=len(self._dimArray), "Dimension component out of range"
        return self._dimArray[dim-1]
    def clear(self,value):
        self._elements.clear(value)
    def __getitem__(self,index) :
        assert len(index ) == len(self._dims)  , "Invalid # of array subscript"
        indexx = self._computeIndex(index)
        assert index is not None ,"Array subscript out of range "
        return self._elements[indexx]
    def __setitem__(self,index,value) :
        assert len(index ) == len(self._dimArray)  , "Invalid # of array subscript"
        indexx = self._computeIndex(index)
        assert index is not None ,"Array subscript out of range "
        self._elements[indexx] = value
    def _computeIndex(self,index):
        offset = 0
        for j in range(len(self._dimArray)):
            if(index[j]<0 or index[j]>= self._dimArray[j]):
                return None 
            offset+= index[j]*self._factors[j]
        return offset

    def _computefactors(self ,dims):
        self._factors[len(dims)-1] = 1
        for i in range(len(dims)) :
            x =1 
            for j in range (i+1,len(dims)):
                x*=dims[j]
            self._factors[i] = x
    def print(self):
        print(self._elements)



