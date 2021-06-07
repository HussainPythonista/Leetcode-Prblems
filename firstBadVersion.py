#Jun 1 2021
def binarySearch(n):
    firstValue=1
    lastValue=n
    while firstValue<lastValue:
        mid=firstValue+lastValue
        if mid==3:

n=5
print(binarySearch(n))

"""if(n==1)
            return 1;
        int low = 1;
        int high = n;
        while(low<=high){
            int mid = low + (high-low)/2;
            if(isBadVersion(mid)){
                // move towards good version
                high = mid-1;
            }else{
                // if good version
				// move towards more recent good version
                low = mid+1;
            }
        }
        return low;
    }
}"""