class Day_Two_Wrapping_Paper
  def initialize
    @running_total =  0
  end

  def run
    puts "Enter dimensions in format 2x3x4\n"
    input_line = gets.chomp
    dimensions = input_line.split('x')
    @x = dimensions[0].to_i
    @y = dimensions[1].to_i
    @z = dimensions[2].to_i
    puts @x
    puts @y
    puts @z
    total = calculate_surface + min_side
    @running_total += total
    puts "#{total} sqft\n"
    puts "Running total: #{@running_total} sqft\n"
  end

  def calculate_surface
    return 2*@x*@y + 2*@x*@z + 2*@y*@z
  end

  def min_side
    side_values = [@x*@y, @x*@z, @y*@z]
    return side_values.min
  end
end

day_two = Day_Two_Wrapping_Paper.new
while true
  day_two.run
end