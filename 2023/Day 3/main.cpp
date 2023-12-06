#include <stdio.h>
#include <iostream>
#include <fstream>

#include <memory>
#include <vector>

constexpr const char * INPUT_FILE_NAME = "/home/scarzer/Projects/AdventOfCode/2023/Day 3/test_input.txt";

struct Point {
    int x;
    int y;
};

class Schematic {
public:
    [[nodiscard]] char GetCharAtXY(size_t x, size_t y ){ return m_schematic[y][x];};
    [[nodiscard]] char GetCharAtPoint(const Point& point){ return GetCharAtXY(point.y,point.x);};

private:
    std::vector<std::vector<char>> m_schematic;
};

class PartNumber {
public: 
    const Point GetLocation() const { return m_location;}
    const int GetNumber() const{ return m_part_number;}

private:
    int m_part_number;
    Point m_location;

    const std::shared_ptr<Schematic> m_schematic;

};

int main(){
    std::string line;
    std::ifstream engine_schematic(INPUT_FILE_NAME);
    
    if (engine_schematic.is_open()) {
        while (getline(engine_schematic, line)){
            std::cout << line << std::endl;
        }
        engine_schematic.close();
    } else {
        std::cout <<"Unable to open the file" << std::endl;
    }
}