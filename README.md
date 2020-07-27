# Red vs Green

This is a simple game where the user is asked to input the initial size of a matrix.
The valid input must be in x,y format where x represents the number of columns and
y - the rows. Then the user is promted to input each row of the matrix. The only 
acceptable values are 0 and 1 with no spaces. Zero is considered Red Cell and one
is Green Cell. Lastly, the user picks a cell and number of generations and inputs
them in the following format: x,y,number_of_generation. Thence, the app applies a set
of rules to generation-zero matrix (the one the user has set) and calculates the state
of the values in the matrix in all the generations upto the given number by the user
inclusively. It counts the number of times the picked cell is in Green state and returns
this number at the end.
