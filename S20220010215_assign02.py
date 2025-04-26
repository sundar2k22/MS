from PIL import Image, ImageDraw, ImageFont

# Load and process the background image
inputImage = Image.open("bg_image.jpg")
width, height = inputImage.size

# Load all images
tree_image = Image.open("tree.jpg")
wishes_image = Image.open("wishes.jpg")
hero_image = Image.open("hero.png")
cloud_image = Image.open("cloud.jpg")

# Resize wishes image
wishes_width = int(width * 0.4)
wishes_height = int(height * 0.1)
wishes_resized = wishes_image.resize((wishes_width, wishes_height), Image.LANCZOS)

# Position wishes image at top center
wishes_x = (width - wishes_width) // 2 - 100
wishes_y = 10

# Resize cloud image for middle placement
cloud_width = int(width * 0.4)  # 30% of width
cloud_height = int(height * 0.2)  # 20% of height
cloud_resized = cloud_image.resize((cloud_width, cloud_height), Image.LANCZOS)

# Position cloud in middle
cloud_x = (width - cloud_width) // 2 + 30
cloud_y = (height - cloud_height) // 2 - 100

# Resize hero image
hero_width = int(width * 0.4)
hero_height = int(height * 0.6)
hero_resized = hero_image.resize((hero_width, hero_height), Image.LANCZOS)

# Position hero at bottom right
hero_x = width - hero_width - 40
hero_y = height - hero_height - 20

# Convert all images to RGBA
wishes_resized = wishes_resized.convert('RGBA')
hero_resized = hero_resized.convert('RGBA')
cloud_resized = cloud_resized.convert('RGBA')
inputImage = inputImage.convert('RGBA')

# Paste wishes image
inputImage.paste(wishes_resized, (wishes_x, wishes_y), wishes_resized)

# Resize tree image
new_tree_width = int(tree_image.width * 0.3)
new_tree_height = int(tree_image.height * 0.3)
tree_image_resized = tree_image.resize((new_tree_width, new_tree_height), Image.LANCZOS)

# Position tree
tree_x = width//2 - new_tree_width - 80
tree_y = height//2 - new_tree_height + 30

# Add all images
tree_image_resized = tree_image_resized.convert('RGBA')
inputImage.paste(tree_image_resized, (tree_x, tree_y), tree_image_resized)
inputImage.paste(cloud_resized, (cloud_x, cloud_y), cloud_resized)
inputImage.paste(hero_resized, (hero_x, hero_y), hero_resized)

# Show final result
# Add text
draw = ImageDraw.Draw(inputImage)
text = "Folks Let's Plant More Trees!!"
font = ImageFont.load_default()

# Calculate text position (centered, above hero image)
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_x = (width - text_width) // 2 + 20
text_y = height - 300  # Position above hero image

# Add shadow effect for better visibility
shadow_offset = 2
draw.text((text_x + shadow_offset, text_y + shadow_offset), 
          text, font=font, fill=(0, 0, 0))  # Shadow
# draw.text((text_x, text_y), text, 
#           font=font, fill=(0, 255, 0))  # Bright yellow text

inputImage.show()
