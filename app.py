import turtle
import math

def setup_screen():
    """Set up the turtle screen"""
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(800, 800)
    screen.title("Symmetric Rangoli Pattern")
    screen.tracer(0)  # Turn off animation for speed
    return screen

def create_turtle():
    """Create and configure turtle"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.pensize(1)
    t.hideturtle()
    return t

def draw_8_sector_circle(t, radius):
    """Draw main circle divided into 8 sectors with alternating yellow and orange colors"""
    sector_colors = ["#ffff00", "#ffa500"]  # Yellow and orange
    
    for i in range(8):
        angle = i * 45  # 360/8 = 45 degrees per sector
        color = sector_colors[i % 2]  # Alternate between yellow and orange
        
        # Draw each sector as a triangle from center
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.pendown()
        
        t.fillcolor(color)
        t.begin_fill()
        
        # Draw sector triangle
        t.forward(radius)
        t.left(135)  # Turn to draw arc
        t.circle(radius, 45)  # Draw 45-degree arc
        t.goto(0, 0)  # Return to center
        
        t.end_fill()
    
    # Draw division lines
    t.pencolor("black")
    t.pensize(2)
    for i in range(8):
        angle = i * 45
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.pendown()
        t.forward(radius)
    
    # Reset pen settings
    t.pencolor("black")
    t.pensize(1)

def draw_outer_ring(t, radius):
    """Draw the outer decorative ring as a proper circle"""
    colors = ["#ff4500", "#ffa500", "#ffff00"]
    
    for i, color in enumerate(colors):
        t.penup()
        t.goto(0, -radius + (i * 8))
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(radius - (i * 8))
        t.end_fill()

def draw_symmetrical_petal(t, radius, angle, colors):
    """Draw a single symmetrical petal"""
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.pendown()
    
    for i, color in enumerate(colors):
        t.fillcolor(color)
        t.begin_fill()
        
        petal_size = radius * (1 - i * 0.15)
        
        # Draw symmetrical petal using forward and arc movements
        t.forward(petal_size * 0.3)
        t.left(45)
        t.forward(petal_size * 0.7)
        t.left(90)
        t.forward(petal_size * 0.4)
        t.left(45)
        t.forward(petal_size * 0.3)
        t.left(90)
        t.forward(petal_size * 0.3)
        t.left(45)
        t.forward(petal_size * 0.4)
        t.left(90)
        t.forward(petal_size * 0.7)
        t.left(45)
        t.forward(petal_size * 0.3)
        t.left(90)
        
        t.end_fill()

def draw_ring_elements(t, radius, num_elements, element_size, colors):
    """Draw symmetrical elements in a ring"""
    for i in range(num_elements):
        angle = i * (360 / num_elements)
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(radius)
        t.pendown()
        
        for j, color in enumerate(colors):
            t.fillcolor(color)
            t.begin_fill()
            
            size = element_size - (j * 3)
            
            # Draw diamond shape
            for _ in range(4):
                t.forward(size)
                t.left(90)
            
            t.end_fill()

def draw_curved_elements(t, radius, num_elements, colors):
    """Draw curved symmetrical elements"""
    for i in range(num_elements):
        angle = i * (360 / num_elements)
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(radius)
        t.pendown()
        
        for j, color in enumerate(colors):
            t.fillcolor(color)
            t.begin_fill()
            
            curve_radius = 15 - (j * 2)
            
            # Draw leaf-like curved shape
            t.circle(curve_radius, 90)
            t.left(90)
            t.circle(curve_radius, 90)
            t.left(180)
            
            t.end_fill()

def draw_main_petals(t):
    """Draw the main 8 petals with perfect symmetry"""
    # Outer layer petals
    outer_colors = ["#8B0000", "#ff0000", "#ff4500", "#ffa500"]
    for i in range(8):
        angle = i * 45
        draw_symmetrical_petal(t, 200, angle, outer_colors)
    
    # Middle layer petals (offset)
    middle_colors = ["#ff0000", "#ff4500", "#ffa500", "#ffff00"]
    for i in range(8):
        angle = i * 45 + 22.5
        draw_symmetrical_petal(t, 160, angle, middle_colors)

def draw_circular_motifs(t, radius, num_motifs, motif_radius, colors):
    """Draw small circular motifs in a ring"""
    for i in range(num_motifs):
        angle = i * (360 / num_motifs)
        
        # Calculate position for each motif
        center_x = radius * math.cos(math.radians(angle))
        center_y = radius * math.sin(math.radians(angle))
        
        # Draw concentric circles for each motif
        for j, color in enumerate(colors):
            t.penup()
            t.goto(center_x, center_y - (motif_radius - j * 2))
            t.pendown()
            t.fillcolor(color)
            t.begin_fill()
            t.circle(motif_radius - j * 2)
            t.end_fill()

def draw_petal_motifs(t, radius, num_motifs, colors):
    """Draw small petal motifs in a ring"""
    for i in range(num_motifs):
        angle = i * (360 / num_motifs)
        
        # Position for each motif
        center_x = radius * math.cos(math.radians(angle))
        center_y = radius * math.sin(math.radians(angle))
        
        # Draw 6-petal flower at each position
        for petal in range(6):
            petal_angle = petal * 60
            t.penup()
            t.goto(center_x, center_y)
            t.setheading(petal_angle)
            t.pendown()
            
            for j, color in enumerate(colors):
                t.fillcolor(color)
                t.begin_fill()
                
                petal_size = 8 - j * 2
                
                # Draw small petal shape
                t.forward(petal_size)
                t.left(60)
                t.forward(petal_size * 0.5)
                t.left(120)
                t.forward(petal_size * 0.5)
                t.left(60)
                t.forward(petal_size)
                t.left(120)
                
                t.end_fill()

def draw_star_motifs(t, radius, num_motifs, colors):
    """Draw small star motifs in a ring"""
    for i in range(num_motifs):
        angle = i * (360 / num_motifs)
        
        # Position for each star
        center_x = radius * math.cos(math.radians(angle))
        center_y = radius * math.sin(math.radians(angle))
        
        # Draw 8-pointed star at each position
        for point in range(8):
            point_angle = point * 45
            t.penup()
            t.goto(center_x, center_y)
            t.setheading(point_angle)
            t.pendown()
            
            for j, color in enumerate(colors):
                t.fillcolor(color)
                t.begin_fill()
                
                point_size = 6 - j * 1.5
                
                # Draw star point
                t.forward(point_size)
                t.left(135)
                t.forward(point_size * 0.4)
                t.left(90)
                t.forward(point_size * 0.4)
                t.left(135)
                t.forward(point_size)
                t.left(180)
                
                t.end_fill()

def draw_mandala_details(t, radius, num_details):
    """Draw intricate mandala details inspired by reference images"""
    for i in range(num_details):
        angle = i * (360 / num_details)
        
        center_x = radius * math.cos(math.radians(angle))
        center_y = radius * math.sin(math.radians(angle))
        
        # Draw teardrop/paisley shapes
        t.penup()
        t.goto(center_x, center_y)
        t.setheading(angle)
        t.pendown()
        
        t.fillcolor("#ff6600")
        t.begin_fill()
        t.circle(8, 180)
        t.left(90)
        t.forward(16)
        t.left(90)
        t.circle(8, 180)
        t.left(90)
        t.forward(16)
        t.end_fill()

def draw_lotus_petals(t, radius, num_petals):
    """Draw lotus petal motifs around a ring"""
    for i in range(num_petals):
        angle = i * (360 / num_petals)
        
        center_x = radius * math.cos(math.radians(angle))
        center_y = radius * math.sin(math.radians(angle))
        
        # Draw lotus petal shape
        t.penup()
        t.goto(center_x, center_y)
        t.setheading(angle)
        t.pendown()
        
        colors = ["#ff4500", "#ffa500"]
        for j, color in enumerate(colors):
            t.fillcolor(color)
            t.begin_fill()
            
            size = 12 - j * 3
            # Draw pointed oval petal
            t.forward(size)
            t.circle(size//2, 90)
            t.forward(size//2)
            t.circle(size//2, 90)
            t.forward(size)
            t.left(180)
            
            t.end_fill()

def draw_decorative_arcs(t, radius, num_arcs):
    """Draw decorative arc patterns"""
    for i in range(num_arcs):
        angle = i * (360 / num_arcs)
        
        center_x = radius * math.cos(math.radians(angle))
        center_y = radius * math.sin(math.radians(angle))
        
        t.penup()
        t.goto(center_x, center_y)
        t.setheading(angle + 45)
        t.pendown()
        
        t.pencolor("#ff0000")
        t.pensize(2)
        t.circle(6, 90)
        
        t.pencolor("black")
        t.pensize(1)

def draw_geometric_triangles(t, radius, num_triangles, colors):
    """Draw geometric triangle patterns inspired by rangoli designs"""
    for i in range(num_triangles):
        angle = i * (360 / num_triangles)
        
        center_x = radius * math.cos(math.radians(angle))
        center_y = radius * math.sin(math.radians(angle))
        
        t.penup()
        t.goto(center_x, center_y)
        t.setheading(angle)
        t.pendown()
        
        for j, color in enumerate(colors):
            t.fillcolor(color)
            t.begin_fill()
            
            side = 10 - j * 2
            # Draw equilateral triangle
            for _ in range(3):
                t.forward(side)
                t.left(120)
            
            t.end_fill()

def draw_intermediate_rings(t):
    """Draw perfectly aligned intermediate rings with enhanced designs"""
    
    # Ring 1: Square elements at outer edge
    draw_ring_elements(t, 240, 24, 12, ["#ff6600", "#ff9900"])
    
    # Ring of circular motifs
    draw_circular_motifs(t, 260, 16, 8, ["#ff4500", "#ffa500", "#ffff00"])
    
    # Ring 2: Diamond elements  
    draw_ring_elements(t, 190, 16, 16, ["#ff0000", "#ff6600"])
    
    # Ring of petal motifs
    draw_petal_motifs(t, 215, 24, ["#ff0000", "#ff6600"])
    
    # Ring 3: Curved leaf elements
    draw_curved_elements(t, 140, 12, ["#ff4500", "#ffa500"])
    
    # Ring of star motifs
    draw_star_motifs(t, 165, 32, ["#ff4500", "#ffa500"])
    
    # Ring 4: Small squares
    draw_ring_elements(t, 110, 24, 8, ["#ffaa00"])
    
    # Add intricate mandala details
    draw_mandala_details(t, 125, 16)
    
    # Add lotus petals between main design elements
    draw_lotus_petals(t, 95, 24)
    
    # Add decorative arcs
    draw_decorative_arcs(t, 85, 32)
    
    # Add geometric triangles
    draw_geometric_triangles(t, 75, 24, ["#ff0000", "#ff6600"])

def draw_center_star(t, radius):
    """Draw perfectly symmetrical 8-pointed star"""
    colors = ["#ff0000", "#ff4500", "#ffa500", "#ffff00"]
    
    for i in range(8):
        angle = i * 45
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.pendown()
        
        # Draw each star point with layers
        for j, color in enumerate(colors):
            t.fillcolor(color)
            t.begin_fill()
            
            point_length = radius * (1 - j * 0.2)
            point_width = radius * 0.3 * (1 - j * 0.2)
            
            # Draw diamond-shaped point
            t.forward(point_length)
            t.left(135)
            t.forward(point_width)
            t.left(90)
            t.forward(point_width)
            t.left(135)
            t.forward(point_length)
            t.left(180)
            
            t.end_fill()

def draw_center_mandala(t):
    """Draw elaborate center mandala - copied from pookalam design"""
    # Center large lotus with 5 layers
    colors = ["#8B0000", "#ff0000", "#ff4500", "#ffa500", "#ffff00"]
    for layer in range(5):
        for petal in range(8):
            petal_angle = petal * 45 + layer * 22.5
            t.penup()
            t.goto(0, 0)
            t.setheading(petal_angle)
            t.pendown()
            
            t.fillcolor(colors[layer])
            t.begin_fill()
            
            petal_size = 30 - layer * 5
            # Elaborate petal
            t.forward(petal_size)
            t.circle(petal_size//4, 60)
            t.forward(petal_size//2)
            t.circle(petal_size//3, 120)
            t.forward(petal_size//2)
            t.circle(petal_size//4, 60)
            t.forward(petal_size)
            t.left(180)
            
            t.end_fill()
    
    # Central circle
    t.penup()
    t.goto(8, 4)
    t.pendown()
    t.fillcolor("#8B0000")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

def draw_center_circle(t, radius):
    """Draw center decorative circle - perfectly aligned"""
    colors = ["#ffff00", "#ffffff"]
    
    for i, color in enumerate(colors):
        t.penup()
        # Perfect center alignment - ensure y coordinate is exactly -radius for each circle
        t.goto(0, -(radius - i * 5))
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.circle(radius - i * 5)
        t.end_fill()

def draw_border_decoration(t):
    """Draw symmetrical border decoration"""
    # Outer border dots
    for i in range(72):
        angle = i * 5
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(285)
        t.pendown()
        
        # Alternating colors
        if i % 3 == 0:
            color = "#ffff00"
        elif i % 3 == 1:
            color = "#ffffff"
        else:
            color = "#ffa500"
        
        t.dot(4, color)

def draw_swirl_patterns(t, radius, num_swirls):
    """Draw swirl patterns inspired by the reference images"""
    for i in range(num_swirls):
        angle = i * (360 / num_swirls)
        
        center_x = radius * math.cos(math.radians(angle))
        center_y = radius * math.sin(math.radians(angle))
        
        t.penup()
        t.goto(center_x, center_y)
        t.setheading(angle)
        t.pendown()
        
        t.fillcolor("#ff4500")
        t.begin_fill()
        
        # Draw spiral/swirl pattern
        for j in range(5):
            t.forward(3 + j)
            t.left(72)
        
        t.end_fill()

def main():
    """Main function to create the symmetric rangoli"""
    screen = setup_screen()
    t = create_turtle()
    
    # Draw from outside to inside for proper layering
    
    # 1. Outer ring background
    draw_outer_ring(t, 300)
    
    # 2. Border decoration
    draw_border_decoration(t)
    
    # 3. NEW: 8-sector main circle (drawn before other elements)
    draw_8_sector_circle(t, 280)
    
    # 4. Intermediate rings (perfectly aligned)
    draw_intermediate_rings(t)
    
    # 5. Main petals (8-fold symmetry)
    draw_main_petals(t)
    
    # 6. Center star (8-fold symmetry)
    draw_center_star(t, 70)
    
    # 7. NEW: Elaborate center mandala (replaces simple center circle)
    draw_center_mandala(t)
    
    # Update screen to show final result
    screen.update()
    
    # Keep window open
    screen.exitonclick()
    print("Click on the screen to exit")

if __name__ == "__main__":
    main()