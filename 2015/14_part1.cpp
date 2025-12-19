#include <iostream>
#include <fstream>
#include <ostream>
#include <string>
#include <sstream>
#include <vector>

struct Reindeer {
    std::string name;
    int speed;
    int flyTime;
    int restTime;
};

std::vector<Reindeer> readInput() {
    std::ifstream input("input_14.in");
    std::string line;
    std::vector<Reindeer> reindeers;

    while (std::getline(input, line)) {
        std::istringstream iss(line);
        Reindeer r;
        std::string word = "";
        iss >> r.name;
        iss >> word >> word;
        iss >> r.speed;
        iss >> word >> word;
        iss >> r.flyTime;
        iss >> word >> word >> word >> word >> word >> word;
        iss >> r.restTime;
        reindeers.push_back(r);
    }

    return reindeers;
}

int main() {
    std::vector<Reindeer> reindeers = readInput();

    for (auto& r : reindeers) {
        std::cout << r.flyTime << " " << r.restTime << " " << r.speed << std::endl;
    }


    std::vector<int> dist(8, 0);

    const auto S = 2503;
    for (auto i=0; i<reindeers.size(); i++) {
        auto& r = reindeers[i];
        long s = 0;
        long sec = 0;

        while (true) {
            s += r.flyTime*r.speed;
            sec += r.flyTime;

            if (S <= sec) {
                std::cout << "BAJ VAN" << std::endl;
                break;
            }

            sec += r.restTime;

            if (S <= sec) {
                dist[i] = s;
                break;
            }
        }
    }

    auto max = 0;
    for (auto& d : dist) {
        if (max < d) {
            max = d;
        }
    }


    std::cout << max << std::endl;

    return 0;
}

