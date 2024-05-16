from flask import Flask , render_template, request
from model import preprocessing_img, predict_result
import traceback 

app = Flask(__name__)
class_names= ['Aloe', 'Corn', 'Guava', 'Hibiscus', 'Lemon', 'Mango', 'Neem', 'Rice', 'Tomato', 'Tulsi']
datas = [
    {
        'scientific name' : 'Aloe vera',
        'Family': 'Asphodelaceae',
        'Average Height': 'Varies; some species are small, while others can grow into large trees',
        'Type': 'Succulent',
        'description': "Aloe vera is a succulent plant species from the genus Aloe. It’s known for its medicinal gel, commonly used in skincare products. Aloe is indigenous to Africa and is grown in arid regions of India, particularly in Rajasthan, Andhra Pradesh, Gujarat, and Maharashtra"
    },
    {
        'scientific name': 'Zea mays',
        'Family': 'Poaceae (Grass family)',
        'Average Height': '4 to 12 feet (1.2-3.6m)',
        'Type': 'Annual grain',
        'description': "Also known as maize, corn is a staple cereal crop originating from the Americas. It’s a tall annual grass widely cultivated for its edible grains. In India, it’s grown mainly in the states of Karnataka, Madhya Pradesh, Bihar, Andhra Pradesh, and Uttar Pradesh"
    },
    {
        'scientific name': 'Psidium guajava',
        'Family': 'Myrtaceae',
        'Average Height': '1 to 30 feet, depending on the growing conditions',
        'Type': 'Evergreen shrub or small tree',
        'description': "Guava is an evergreen shrub or small tree native to the Caribbean, Central America, and South America. It bears sweet and fragrant fruits and is commonly found in the tropical and subtropical regions of India, especially in Uttar Pradesh, Bihar, Maharashtra, and Karnataka2"
    },
    {
        'scientific name': 'Hibiscus rosa-sinensis',
        'Family': 'Malvaceae (Mallow family)',
        'Average Height': 'Varies widely; some species can grow up to 15 feet tall',
        'Type': 'Herbs, shrubs, and trees',
        'description': "Known for its large, colorful, and showy flowers, hibiscus is a genus of flowering plants in the mallow family. It’s native to warm temperate, subtropical, and tropical regions worldwide. In India, it’s popular as an ornamental plant and grows abundantly in the warmer regions"
    },
    {
        'scientific name': "Citrus limon",
        "Family": "Rutaceae",
        "Average Height": "10 to 20 feet",
        "Type": "Evergreen tree",
        'description': "Lemon is a small evergreen tree bearing tart, yellow citrus fruits. It’s part of the citrus genus and is widely cultivated in tropical and subtropical climates. In India, lemons are grown in almost all parts, with Andhra Pradesh, Maharashtra, Tamil Nadu, Gujarat, and Rajasthan being the leading producers"
    },
    {
        'scientific name': 'Mangifera indica',
        'Family': 'Anacardiaceae',
        'Average Height': '10 to 100 feet',
        'Type': 'Evergreen tree',
        'description': "Mango, the king of fruits, is indigenous to the Indian subcontinent and is widely cultivated in tropical regions. It’s a large fruit-bearing tree known for its sweet fruit. In India, mangoes are primarily grown in Uttar Pradesh, Andhra Pradesh, Karnataka, Bihar, Gujarat, and Telangana"
    },
    {
        'scientific name': 'Azadirachta indica',
        'Family': 'Meliaceae (Mahogany family)',
        'Average Height': '49 to 80 feet',
        'Type': 'Evergreen tree',
        'description': "Neem, also known as Indian lilac, is a tree in the mahogany family Meliaceae. It’s valued for its medicinal properties and is native to the Indian subcontinent. Neem trees are found throughout India, particularly in rural areas where they are often planted around homes"
    },
    {
        'scientific name': 'Oryza sativa',
        'Family': 'Poaceae (Grass family)',
        'Average Height':'0.4 to more than 5 meters',
        'Type': 'Annual grass',
        'description': "Rice is a staple food for more than half of the world’s population. It’s an annual grass producing edible starchy grains. India is one of the largest producers of rice, with significant cultivation in states like West Bengal, Uttar Pradesh, Punjab, Andhra Pradesh, and Telangana"
    },
    {
        "scientific name": "Solanum lycopersicum",
        "Family": "Solanaceae (Nightshade family)",
        "Average Height": "3 to 10 feet, depending on the variety",
        "Type": "Annual fruiting plant",
        'description':"Tomato is an edible berry of the nightshade family, native to western South America. It’s a staple vegetable-fruit across the globe. In India, tomatoes are extensively cultivated with major production in states like Andhra Pradesh, Karnataka, Madhya Pradesh, and Maharashtra"
    },
    {
        "scientific name": "Ocimum tenuiflorum",
        "Family": "Lamiaceae (Mint family)",            
        "Average Height": "1 to 3 feet",
        "Type": "Perennial or annual herbaceous plant",
        'description': "Also known as holy basil, Tulsi is an aromatic perennial plant in the Lamiaceae family. It’s native to the Indian subcontinent and is revered for its medicinal properties. Tulsi is widely cultivated throughout India for religious and traditional medicine purposes"
    },
    ]
@app.route('/')
def main():
    return render_template('index.html')

# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            img = preprocessing_img(request.files['file'].stream)
            class_index, probability = predict_result(img)
            class_name = class_names[class_index]  # Assuming class_names is a list of class names
            data = datas[class_index]
            return render_template("result.html", class_name=class_name, probability=probability, des=data)
 
    except Exception as e:
        error = "File cannot be processed."
        print(traceback.format_exc())
        return render_template("result.html", err=error)

# Driver code
if __name__ == '__main__':
    app.run(port=9000, debug=True)