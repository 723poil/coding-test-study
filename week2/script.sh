#!/bin/bash

directories=(
    "01.분해합"
    "02.일곱난쟁이"
    "03.바이러스"
    "04.DFS와 BFS"
    "05.유기농 배추"
    "06. 음식물 피하기"
    "07.미로탐색"
    "08.토마토"
    "09.벽 부수고 이동하기"
    "10.왕실의 기사 대결"
)

for dir in "${directories[@]}"; do
    mkdir -p "$dir" && touch "$dir/.gitkeep" # Create directory and file
done
