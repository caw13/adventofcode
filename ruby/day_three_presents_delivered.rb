class Day_Three_Presents_Delivered
  def run
    puts "Enter input:\n"
    input_line = gets.chomp
    @coord_x = 0
    @coord_y = 0
    present_locations = Hash.new
    present_locations[get_key]=1
    input_line.each_char {|c|
      if c == ">"
        @coord_x += 1
      elsif c == "<"
        @coord_x -= 1
      elsif c =='^'
        @coord_y += 1
      else
        @coord_y -= 1
      end
      present_locations[get_key]=1
    }
    puts "Unique houses: #{present_locations.keys.size}"
  end

  def get_key
    return "#{@coord_x}-#{@coord_y}"
  end
end

day_three = Day_Three_Presents_Delivered.new
while true
  day_three.run
end