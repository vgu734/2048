import random

class Game:
    '''
    A class representing a game.
    
    Attributes:
    size (int): The NxN size of the board
    p_two: probability of randomly generating a two
    tiles: list of tiles
    score: Player score
    '''
    size = 5
    p_two = .85
    
    def __init__(self, score=0):
        self.tiles = self.initTiles()
        self.score = score
        
    def initTiles(self):
        tiles = []
        for i in range(self.size):
            for j in range(self.size):
                tiles.append(Tile(index=(i, j)))
                
        random.choice(tiles).value = 2 if random.random() < self.p_two else 4
        return tiles
    
    def moveLeft(self):
        '''
        Simulates left move.
        '''
        for i in range(self.size):
            row = [tile for tile in self.tiles if tile.index[0] == i]
            values = [tile.value for tile in row]
            
            compressed_values = self.compress(values)
            merged_values = self.merge(compressed_values)
            final_values = self.compress(merged_values)
            self.update_tile_values(row, final_values)
            
    def moveRight(self):
        '''
        Simulates right move.
        '''
        for i in range(self.size):
            row = [tile for tile in self.tiles if tile.index[0] == i]
            values = [tile.value for tile in row]
            values = values[::-1]
            
            compressed_values = self.compress(values)
            merged_values = self.merge(compressed_values)
            final_values = self.compress(merged_values)
            self.update_tile_values(row, final_values[::-1])
        
    def moveUp(self):
        '''
        Simulates up move. Swaps indicies for rows and columns to make it easier.
        '''
        for j in range(self.size):
            col = sorted([tile for tile in self.tiles if tile.index[1] == j], key=lambda t: t.index[0])
            values = [tile.value for tile in col]
            
            compressed_values = self.compress(values)
            merged_values = self.merge(compressed_values)
            final_values = self.compress(merged_values)
            
            self.update_tile_values(col, final_values)
        
    def moveDown(self):
        '''
        Simulates down move.
        '''
        for j in range(self.size):
            col = sorted([tile for tile in self.tiles if tile.index[1] == j], key=lambda t: t.index[0], reverse=True)
            values = [tile.value for tile in col]
            
            compressed_values = self.compress(values)
            merged_values = self.merge(compressed_values)
            final_values = self.compress(merged_values)
            
            self.update_tile_values(col, final_values)

    def compress(self, values):
        '''
        Simulates compression (e.g. moving all the tiles to the farthest in any direction)
        
        Parameters:
        values (list[int]): List, ordered by index, of tile values
        
        Returns:
        compressed (list[int]): List, ordered by index, of tile values after compression
        '''
        non_zero_values = [value for value in values if value != 0]
        compressed = [0] * len(values)
        index = 0
        for value in non_zero_values:
            compressed[index] = value
            index += 1
        return compressed
    
    def merge(self, values):
        '''
        Simulate merge (e.g. during player move, merge tiles of same value along line of movement).
        Also increases player score according to the summation of merged tile values.
        
        Parameters:
        values (list[int]): List, ordered by index, of tile values prior to merge
        
        Returns:
        values (list[int]): List, ordered by index, of tile values after the merge
        '''
        for i in range(len(values) - 1):
            if values[i] == values[i + 1] and values[i] != 0:
                self.score += values[i]
                values[i] *= 2
                values[i + 1] = 0
        return values
    
    def update_tile_values(self, tiles, new_values):
        '''
        Update given tiles with new values.
        
        Parameters:
        tiles (list[tile]): List of tiles in the previous game state
        new_values (list[int]): List of new values to update the tiles to the current game state
        '''
        for i, tile in enumerate(tiles):
            tile.value = new_values[i]
        
        
class Tile:
    '''
    A class representing a tile.
    
    Attributes:
    index (int, int): Tile index (r,c)
    value (int): Tile value
    '''
    def __init__(self, index, value=0):
        self.index = index
        self.value = value
        
    def __repr__(self):
        return f"Tile(index={self.index}, value={self.value})"
    
    def __eq__(self, other):
        return self.index == other.index and self.value == other.value