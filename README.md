# Command Line Tools
Just some hopefully useful command line tools

- ## Rand - Generate SECURE random passwords or numbers
    
        usage: rand [-h] -t {password,number} [-l LENGTH] [-c {weak,moderate,strong,extreme}] [-a AMOUNT]
        Generate SECURE random passwords or numbers
        
        optional arguments:
        -h, --help            show this help message and exit
        -t {password,number}, --type {password,number}
                              Generate either a random password or a random number
        -l LENGTH, --length LENGTH
                              Defines either the password length or maximum possible random number value in 'length' bits 
                              Note: Passwords will always be at least 8 characters long
        -c {weak,moderate,strong,extreme}, --complexity {weak,moderate,strong,extreme}
                              Complexity defines the inclusion of uppercase characters, numbers or symbols variability.
                              Note: argument ignored when generating random numbers
        -a AMOUNT, --amount AMOUNT
                              Controls how many random passwords or numbers to generate