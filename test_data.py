
import random
from datetime import date, datetime, time

blog_posts = [
    {
        'id': 1,
        'title': 'The Rise of AI: Opportunities and Challenges',
        'author': 'Jane Doe',
        'content': 'Artificial intelligence is transforming industries around the globe. This post explores the opportunities and challenges that AI brings.',
        'date_posted': '2024-05-01'
    },
    {
        'id': 2,
        'title': 'Exploring the Benefits of a Plant-Based Diet',
        'author': 'John Smith',
        'content': 'A plant-based diet offers numerous health benefits. Learn how to transition to a plant-based diet and the positive effects it can have.',
        'date_posted': '2024-05-02'
    },
    {
        'id': 3,
        'title': 'Top 10 Travel Destinations for 2024',
        'author': 'Emily Johnson',
        'content': 'Planning your next vacation? Check out our list of the top 10 travel destinations for 2024.',
        'date_posted': '2024-05-03'
    },
    {
        'id': 4,
        'title': 'How to Improve Your Mental Health',
        'author': 'Michael Brown',
        'content': 'Mental health is crucial for overall well-being. Here are some tips and strategies to improve your mental health.',
        'date_posted': '2024-05-04'
    },
    {
        'id': 5,
        'title': 'The Future of Electric Vehicles',
        'author': 'Sarah Davis',
        'content': 'Electric vehicles are the future of transportation. Discover the latest advancements and trends in the EV industry.',
        'date_posted': '2024-05-05'
    },
    {   'id': 6,
        'title': 'A Guide to Minimalist Living',
        'author': 'David Wilson',
        'content': 'Embrace minimalist living to simplify your life and reduce stress. This guide will help you get started.',
        'date_posted': '2024-05-06'
    },
    {   
        'id': 7,
        'title': 'The Importance of Cybersecurity in Today’s World',
        'author': 'Laura Martinez',
        'content': 'As technology advances, so do cybersecurity threats. Learn why cybersecurity is more important than ever and how to protect yourself.',
        'date_posted': '2024-05-07'
    },
    {
        'id': 8,
        'title': 'Healthy Eating on a Budget',
        'author': 'Robert Garcia',
        'content': 'Eating healthy doesn’t have to be expensive. Find out how you can maintain a nutritious diet without breaking the bank.',
        'date_posted': '2024-05-08'
    },
    {
        'id': 9,
        'title': 'The Benefits of Remote Work',
        'author': 'Jessica Rodriguez',
        'content': 'Remote work offers flexibility and work-life balance. Explore the benefits of remote work and how to make the most of it.',
        'date_posted': '2024-05-09'
    },
    {
        'id': 10,
        'title': 'The Art of Mindfulness: Techniques and Benefits',
        'author': 'Daniel Lee',
        'content': 'Mindfulness can improve your mental and physical health. Learn techniques and benefits of practicing mindfulness.',
        'date_posted': '2024-05-10'
    },
    {
        'id': 11,
        'title': 'Renewable Energy Sources: The Path to a Sustainable Future',
        'author': 'Susan Clark',
        'content': 'Renewable energy is key to combating climate change. Discover different renewable energy sources and their impact on the environment.',
        'date_posted': '2024-05-11'
    },
    {
        'id': 12,
        'title': 'How to Build a Successful Online Business',
        'author': 'James Lewis',
        'content': 'Building an online business can be rewarding and profitable. Follow these steps to create and grow a successful online business.',
        'date_posted': '2024-05-12'
    },
    {
        'id': 13,
        'title': 'The Role of Education in Personal and Professional Growth',
        'author': 'Patricia Walker',
        'content': 'Education is vital for personal and professional development. Learn about the different ways education can impact your life.',
        'date_posted': '2024-05-13'
    },
    {
        'id': 14,
        'title': 'The Impact of Social Media on Society',
        'author': 'Thomas Hall',
        'content': 'Social media has a significant impact on society. Explore the positive and negative effects of social media usage.',
        'date_posted': '2024-05-14'
    },
    {
        'id': 15,
        'title': 'Investing 101: A Beginner’s Guide',
        'author': 'Linda Harris',
        'content': 'Investing can help you build wealth over time. This beginner’s guide will teach you the basics of investing.',
        'date_posted': '2024-05-15'
    },
    {
        'id': 16,
        'title': 'The Evolution of Technology in the Last Decade',
        'author': 'Barbara Young',
        'content': 'Technology has evolved rapidly over the past decade. Take a look at the most significant technological advancements.',
        'date_posted': '2024-05-16'
    },
    {
        'id': 17,
        'title': 'Fitness Tips for a Healthier Lifestyle',
        'author': 'Paul King',
        'content': 'Staying fit is essential for a healthy lifestyle. Here are some fitness tips to help you stay in shape.',
        'date_posted': '2024-05-17'
    },
    {
        'id': 18,
        'title': 'The Importance of Financial Literacy',
        'author': 'Nancy Wright',
        'content': 'Financial literacy is crucial for managing your finances effectively. Learn why financial literacy is important and how to improve yours.',
        'date_posted': '2024-05-18'
    },
    {
        'id': 19,
        'title': 'The Power of Positive Thinking',
        'author': 'Richard Green',
        'content': 'Positive thinking can transform your life. Discover the power of positivity and how to cultivate a positive mindset.',
        'date_posted': '2024-05-19'
    },
    {
        'id': 20,
        'title': 'The Future of Work: Trends and Predictions',
        'author': 'Karen Adams',
        'content': 'The future of work is evolving. Explore the trends and predictions shaping the future of work.',
        'date_posted': '2024-05-20'
    }
]


post_id = random.randint(1, 21)


def post(id):
    id = id
    for item in blog_posts:
        if item['id'] == post_id:
            post = item
            print(post)

post(post_id)


post_date = date.today().strftime("%B %d, %Y")
print(post_date)

from datetime import datetime

# Get the current date and time
now = datetime.now().replace(microsecond=0)

# Remove the milliseconds (microseconds)
now_without_microseconds = now.replace(microsecond=0)

print("Original datetime:", now)
print("Datetime without milliseconds:", now_without_microseconds)

print(f"Now: {now}")


