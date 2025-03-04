class Calculator :
	# return the sum between 2 operands
	def mysum(self, first_operand, second_operand):
		return first_operand + second_operand

    
	# return the mean between 2 operands
	def mymean(self, first_operand, second_operand):
		return (first_operand+second_operand) / 2

	# return the minimum
	def mymin(self, first, second):
		return first if first <= second else second

	# return the maximum
	def mymax(self, first, second):
		return first if first > second else second

