OBJECTS = main.o Term.o Autocomplete.o
HEADERS = Term.h Autocomplete.h
CS216PA3: $(OBJECTS)
	g++ $^ -o CS216PA3
%.o: %.cpp $(HEADERS)
	g++ -c $< -o $@
clean:
	rm -i *.o CS216PA3
