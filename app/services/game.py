import random

class Game:
    size = 5
    
    def __init__(self, score=0):
        self.tiles = self.initTiles()
        self.score = score
        
    def initTiles(self):
        tiles = []
        for i in range(self.size):
            for j in range(self.size):
                tiles.append(Tile(index=(i, j)))
                
        random.choice(tiles).value = 2 if random.random() < .8 else 4
        return tiles
    
    def moveLeft(self):
        for i in range(self.size):
            row = [tile for tile in self.tiles if tile.index[0] == i]
            values = [tile.value for tile in row]
            
            compressed_values = self.compress(values)
            merged_values = self.merge(compressed_values)
            final_values = self.compress(merged_values)
            self.update_tile_values(row, final_values)
            
    def moveRight(self):
        for i in range(self.size):
            row = [tile for tile in self.tiles if tile.index[0] == i]
            values = [tile.value for tile in row]
            values = values[::-1]
            
            compressed_values = self.compress(values)
            merged_values = self.merge(compressed_values)
            final_values = self.compress(merged_values)
            self.update_tile_values(row, final_values[::-1])
        
    def moveUp(self):
        for j in range(self.size):
            col = sorted([tile for tile in self.tiles if tile.index[1] == j], key=lambda t: t.index[0])
            values = [tile.value for tile in col]
            
            compressed_values = self.compress(values)
            merged_values = self.merge(compressed_values)
            final_values = self.compress(merged_values)
            
            self.update_tile_values(col, final_values)
        
    def moveDown(self):
        for j in range(self.size):
            col = sorted([tile for tile in self.tiles if tile.index[1] == j], key=lambda t: t.index[0], reverse=True)
            values = [tile.value for tile in col]
            
            compressed_values = self.compress(values)
            merged_values = self.merge(compressed_values)
            final_values = self.compress(merged_values)
            
            self.update_tile_values(col, final_values)

    def compress(self, values):
        non_zero_values = [value for value in values if value != 0]
        compressed = [0] * len(values)
        index = 0
        for value in non_zero_values:
            compressed[index] = value
            index += 1
        return compressed
    
    def merge(self, values):
        for i in range(len(values) - 1):
            if values[i] == values[i + 1] and values[i] != 0:
                values[i] *= 2
                values[i + 1] = 0
        return values
    
    def update_tile_values(self, tiles, new_values):
        for i, tile in enumerate(tiles):
            tile.value = new_values[i]
        
        
class Tile:
    def __init__(self, index, value=0):
        self.index = index #(r, c)
        self.value = value
        
    def __repr__(self):
        return f"Tile(index={self.index}, value={self.value})"