#include <iostream>
#include <string>

#include "Additive-Cypher.hxx"
#include "Single-Columnar-Cypher.hxx"

std::string ProductCypher (const std::string& p_text, const char additive_key, const std::string& columnar_key)
{
   auto const c_additive = AdditiveCypher (p_text, additive_key);
   auto const c_columnar = SingleColumnarCypher (p_text, columnar_key);
   return c_columnar;
}
std::string ProductDeCypher (const std::string& c_text, const char additive_key, const std::string& columnar_key)
{
   auto const p_additive = AdditiveDecypher (c_text, additive_key);
   auto const p_columnar = SingleColumnarDecypher (c_text, columnar_key);
   return p_columnar;
}

int main ()
{
   const auto additive_key = 5;
   const auto columnar_key = "zebras";
   auto const c_text = ProductCypher ("WE ARE DISCOVERED FLEE AT ONCE", additive_key, columnar_key);
   std::cout << "Encrypted : " << c_text;
   std::cout << "\nDecrypted " << ProductDeCypher (c_text, additive_key, columnar_key);
   return 0;
}