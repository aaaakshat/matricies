# Time Bound Computatin: Matrix Multiplication
## Process
My script asks for a user input for the size of the nxn matrix to be randomly generated. The script iterates through a variable amount of nxn matricies until the set size and plots out the resulting graph for both my algorithm and numpy.

## Results
Looking at the results for the smaller iterations — namely random matricies up till 50x50 we get rather fluctuating results:

#### Up to 50x50 Matrix test #1
![up to 50x50 matrix](https://raw.githubusercontent.com/aaaakshat/matricies/master/media/50.png)
#### Up to 50x50 Matrix test #2
![up to 50 matrix](https://raw.githubusercontent.com/aaaakshat/matricies/master/media/50-2.png)

Though the numpy algorithm is faster, for smaller matricies it appears that there are significant fluctuations — this is most likely due to the fact that my transposition function uses zip which could be applied faster or slower depending on the input matrix.

### Larger Matricies
For larger matricies the curve appears to gradually flatten out and there is a fixed gap between the numpy algorithm and my results. I believe this is due to the fact that as the matricies get larger and larger my algorithm is bottlenecked by the fact that it first tranposes then multiplys the arrays together, resulting 2 stages of nested loops which I believe creates a fixed bottleneck for each nxn matrix (though for extremly large matricies I would expect numpy to be more optimised).

![up to 100x100 matrix](https://raw.githubusercontent.com/aaaakshat/matricies/master/media/100.png)
![up to 120x120 matrix](https://raw.githubusercontent.com/aaaakshat/matricies/master/media/120.png)
