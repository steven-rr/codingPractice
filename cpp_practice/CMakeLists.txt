# Initial setup
cmake_minimum_required(VERSION 3.10)
project(cpp_practice)

# for additional files aside from maincpp
add_library(linkedlist
            linkedlist.cpp
            linkedlist.h)

#executable from main cpp file.
add_executable(cpp_practice main.cpp)

# Set Xcode properties when running in APPLE.
if (APPLE)
   set_target_properties(cpp_practice PROPERTIES
              CMAKE_XCODE_GENERATE_SCHEME TRUE
              XCODE_GENERATE_SCHEME TRUE
              XCODE_SCHEME_WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
endif()

#add library subdirectory.
add_subdirectory(data_structures)
# link library to subdirectory
target_link_libraries(cpp_practice PUBLIC linkedlist data_structures)
# make sure that the path is included 
target_include_directories(cpp_practice PUBLIC ${CMAKE_SOURCE_DIR}/data_structures)