input-format:

* each line is a problem
* entries in a line separated by semicolon ;
* entries in line:
    * id of input-sample
    * number of contracts
    * number of variants
    * qubo: size = (number of contracts * number of variants)^2
        - qubo-entries separated by comma ,
        - qubo-entry is a floating point number
    * profit-list: size= number of contracts * number of variants
        - profit-list-entries seperated by comma,
        - profit-list-entry is a floating point number