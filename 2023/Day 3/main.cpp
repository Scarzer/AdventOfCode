#include <stdio.h>
#include <iostream>
#include <fstream>

#include <memory>
#include <vector>
#include <map>

constexpr const char * INPUT_FILE_NAME = "/home/scarzer/Projects/AdventOfCode/2023/Day 3/test_input.txt";

const std::map<char, int> NUMBERS = { {'0', 0},  {'1', 1}, {'2', 2}, {'3', 3}, {'4', 4}, {'5', 5}, {'6', 6}, {'7', 7}, {'8', 8}, {'9', 9}};

class Schematic;

struct Point {
    int x;
    int y;
};

class PartNumber {
public: 
    const Point GetLocation() const { return m_location;}
    const int GetNumber() const{ return m_partNumber;}

private:
    int m_partNumber;
    Point m_location;
    std::string m_rawNumber;       

    const std::shared_ptr<Schematic> m_schematic;

};


class Schematic {
public:
    Schematic(std::vector<std::string> schematic)
        : m_schematic{schematic}{

            for(auto schematicRow = 0; schematicRow < schematic.size(); schematicRow++){
                std::string number = "";
                bool found_number = false;
                for (auto element = 0; element < m_schematic[schematicRow].size(); element++){
                    
                    auto schematicElement = m_schematic[schematicRow][element];
                    if(!found_number && schematicElement == '.'){
                        // We're not in the middle of a number and we've got a '.'. Move on
                        continue;
                    } else if (found_number && schematicElement == '.'){
                        // We were following a number but we've gotten it now. Finish it. 
                        found_number = false;
                        auto converted_number = atoi(number.c_str());
                        m_numbers.push_back(converted_number);
                        std::cout << "Found a number " << converted_number << std::endl;
                        number = "";
                    } else if (NUMBERS.count(schematicElement) > 0){
                        // We've found a number, so add it to the found number
                        number+=schematicElement;
                        found_number = true;
                        continue;
                    }else {
                        std::cout << "Found a symbol " << schematicElement << std::endl;
                    }
                }
            }
        }

    [[nodiscard]] char GetCharAtXY(size_t x, size_t y ){ return m_schematic[y][x];}
    [[nodiscard]] char GetCharAtPoint(const Point& point){ return GetCharAtXY(point.y,point.x);}

    std::vector<PartNumber> GetPartNumbers(){
        return std::vector<PartNumber>{};
    }

private:
    std::vector<std::string> m_schematic;
    std::vector<PartNumber> m_partNumbers;
    std::vector<int> m_numbers;
};
/////////////////////////////////////////////////////////

int main(){
    std::string line;
    std::ifstream engine_schematic(INPUT_FILE_NAME);
    
    std::vector<std::string> schematic;
    if (engine_schematic.is_open()) {
        while (getline(engine_schematic, line)){
            schematic.push_back(line);
        }
        engine_schematic.close();
    } else {
        std::cout <<"Unable to open the file" << std::endl;
    }

    auto schem = Schematic(schematic);

}