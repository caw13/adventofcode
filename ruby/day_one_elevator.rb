class Day_One_Elevator

  def run
    puts "Enter elevator directions:\n"
    input_line = gets
    !input_line.chomp
    cur_floor = 0
    input_line.each_char {|c|
      if c == ")"
        # puts "down"
        cur_floor -= 1
      elsif c == "("
        # puts "up"
        cur_floor += 1
      end
    }
    puts "Resulting floor #{cur_floor}"
  end
end

elevator = Day_One_Elevator.new
while true
  elevator.run
end