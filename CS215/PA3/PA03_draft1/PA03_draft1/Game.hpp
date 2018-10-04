//
//  Game.hpp
//  PA03_draft1
//
//  Created by Kelly Sovacool on 11/10/15.
//  Copyright © 2015 Kelly Sovacool. All rights reserved.
//

#ifndef Game_hpp
#define Game_hpp
#include <string>
#include <iostream>
using namespace std;
class Game {
    public:
        Game(string n, int c, double p, double s):name(n), count(c), price(p), score(s) {}
    private:
        string name; //game name
        int count; //number of copies in stock
        double price; //game price
        double score; //user score, in the range [0, 10.0]
    friend class GameList;
};
#endif /* Game_hpp */
