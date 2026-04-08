def calculate_pyramid_height(number_of_blocks):
    height = 0
    blocks_needed = 1 # İlk kat için gereken blok
    
    while number_of_blocks >= blocks_needed:
        number_of_blocks -= blocks_needed
        height += 1
        blocks_needed += 1 # Bir sonraki kat bir öncekinden 1 fazla blok ister
        
    return height
