#include <iostream>
using namespace std;

void colorprint(string color, string text) {
  string black = "0;30m";
  string red = "1;31m";
  string green = "1;32m";
  string yellow = "1;33m";
  string blue = "1;34m";
  string purple = "1;35m";
  string cyan = "1;36m";
  string white = "1;37m";
  string clr = "\033[";
  string end = "\033[0m\n";
  if (color == "black") {cout << clr << black << text << end;}
  if (color == "red") {cout << clr << red  << text << end;}
  if (color == "green") {cout << clr << green << text << end;}
  if (color == "yellow") {cout << clr << yellow << text << end;}
  if (color == "blue") {cout << clr << blue << text << end;}
  if (color == "purple") {cout << clr << purple << text << end;}
  if (color == "cyan") {cout << clr << cyan << text << end;}
  if (color == "white") {cout << clr << white << text << end;}
}
