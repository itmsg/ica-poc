class Problem:

    def __init__(self):
        self.id = ""
        self.number_of_contracts = 0
        self.number_of_variants = 0
        self.qubo_as_string =""
        self.profit_as_string=""
        self.qubo_as_array= None

    def to_string(self,detailed):
       line = "\n"+ "----------------"
       id = line + "\n"+ "problem: " + self.id + line
       description = "contracts|variants" + str(self.number_of_contracts)+ "|" + str(self.number_of_variants)
       return str(id) + "\n" + description + "\n" + str(self.qubo_as_array) + line

    def init_problem_from_csv_line(self,row):
        self.id = row["id"]
        self.number_of_contracts = int(row["contracts"])
        self.number_of_variants = int(row["variants"])
        self.qubo_as_string = row["qubo"]
        self.profit_as_string = row["profit"]
        self.set_qubo_as_array_fromqubo_as_string(row["qubo"])
        return self

    def set_qubo_as_array_fromqubo_as_string(self, qubo_string):
        entry_array = qubo_string.split(',')
        entry_array = list(map(lambda x: x.replace('_', '0.0'), entry_array))
        entry_array_with_float_entries=[float(i) for i in entry_array]
        entries_per_line= int(self.number_of_variants*self.number_of_contracts)
        self.qubo_as_array = [entry_array_with_float_entries[i *entries_per_line:(i + 1) * entries_per_line] for i in range((len( entry_array_with_float_entries) + entries_per_line - 1) // entries_per_line)]



    def set_fieldvalue(self, value):
        if self.is_input and self.fieldvalue != value:
            self.has_conflict = True
        elif not self.is_input:
            self.fieldvalue = value

    def replace_field(self, new_field):
        self.fieldvalue = new_field.value
        self.is_input = new_field.input
        self.has_conflict = new_field.confilict

    def is0(self):
        return self.fieldvalue == 0

    def reset(self):
        #print("FIELD RESET")
        self.fieldvalue = 0
        self.is_input = False
        self.has_conflict = False
        #print(self.fieldvalue, self.is_input)


