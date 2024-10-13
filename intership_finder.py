import json
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle

# Sample data for internships
internships = [
    # Computer Science
    {"title": "Software Engineering Intern", "skills": ["Python", "Teamwork"], "location": "Remote", "industry": "Computer Science"},
    {"title": "Data Science Intern", "skills": ["Python", "Machine Learning"], "location": "Dallas", "industry": "Computer Science"},
    {"title": "Web Development Intern", "skills": ["HTML", "CSS", "JavaScript"], "location": "Arlington", "industry": "Computer Science"},
    {"title": "Mobile App Development Intern", "skills": ["Java", "Kotlin"], "location": "Irving", "industry": "Computer Science"},
    {"title": "IT Support Intern", "skills": ["Troubleshooting", "Customer Service"], "location": "Plano", "industry": "Computer Science"},
    {"title": "Machine Learning Intern", "skills": ["Python", "Data Analysis"], "location": "Remote", "industry": "Computer Science"},
    {"title": "Game Development Intern", "skills": ["C++", "Unity"], "location": "Frisco", "industry": "Computer Science"},
    {"title": "Cloud Computing Intern", "skills": ["AWS", "Python"], "location": "Dallas", "industry": "Computer Science"},
    {"title": "Cybersecurity Intern", "skills": ["Security Protocols", "Python"], "location": "Plano", "industry": "Computer Science"},
    {"title": "Network Engineering Intern", "skills": ["Networking", "Troubleshooting"], "location": "Arlington", "industry": "Computer Science"},
    {"title": "Database Management Intern", "skills": ["SQL", "Database Design"], "location": "Irving", "industry": "Computer Science"},
    {"title": "Front-End Development Intern", "skills": ["JavaScript", "React"], "location": "Remote", "industry": "Computer Science"},
    {"title": "Back-End Development Intern", "skills": ["Node.js", "Express"], "location": "Frisco", "industry": "Computer Science"},
    {"title": "AI Research Intern", "skills": ["Machine Learning", "Research"], "location": "Remote", "industry": "Computer Science"},
    {"title": "Technical Support Intern", "skills": ["Customer Service", "Troubleshooting"], "location": "Plano", "industry": "Computer Science"},
    {"title": "Data Analysis Intern", "skills": ["Python", "Statistics"], "location": "Dallas", "industry": "Computer Science"},
    {"title": "Software Testing Intern", "skills": ["QA", "Automation"], "location": "Arlington", "industry": "Computer Science"},
    {"title": "Robotics Intern", "skills": ["Arduino", "Programming"], "location": "Frisco", "industry": "Computer Science"},
    {"title": "Blockchain Intern", "skills": ["Cryptography", "Smart Contracts"], "location": "Remote", "industry": "Computer Science"},
    {"title": "DevOps Intern", "skills": ["CI/CD", "Linux"], "location": "Irving", "industry": "Computer Science"},
    
    # Business
    {"title": "Marketing Intern at Tech Start-up", "skills": ["Communication", "Creativity"], "location": "Frisco", "industry": "Business"},
    {"title": "Financial Analyst Intern", "skills": ["Excel", "Data Analysis"], "location": "Dallas", "industry": "Business"},
    {"title": "Sales Intern", "skills": ["Communication", "Negotiation"], "location": "Irving", "industry": "Business"},
    {"title": "Human Resources Intern", "skills": ["Organizational Skills", "Communication"], "location": "Dallas", "industry": "Business"},
    {"title": "Product Management Intern", "skills": ["Analytical Skills", "Teamwork"], "location": "Plano", "industry": "Business"},
    {"title": "Business Development Intern", "skills": ["Networking", "Research"], "location": "Frisco", "industry": "Business"},
    {"title": "Accounting Intern", "skills": ["Excel", "Bookkeeping"], "location": "Dallas", "industry": "Business"},
    {"title": "Market Research Intern", "skills": ["Research", "Data Analysis"], "location": "Irving", "industry": "Business"},
    {"title": "Public Relations Intern", "skills": ["Communication", "Writing"], "location": "Plano", "industry": "Business"},
    {"title": "Event Planning Intern", "skills": ["Organization", "Communication"], "location": "Frisco", "industry": "Business"},
    {"title": "Social Media Intern", "skills": ["Content Creation", "Marketing"], "location": "Remote", "industry": "Business"},
    {"title": "Business Analyst Intern", "skills": ["Data Analysis", "Reporting"], "location": "Dallas", "industry": "Business"},
    {"title": "Customer Service Intern", "skills": ["Communication", "Problem-Solving"], "location": "Arlington", "industry": "Business"},
    {"title": "Operations Intern", "skills": ["Analytical Skills", "Organization"], "location": "Irving", "industry": "Business"},
    {"title": "Digital Marketing Intern", "skills": ["SEO", "Content Writing"], "location": "Plano", "industry": "Business"},
    {"title": "Strategy Intern", "skills": ["Analytical Skills", "Research"], "location": "Frisco", "industry": "Business"},
    {"title": "Investment Intern", "skills": ["Finance", "Research"], "location": "Dallas", "industry": "Business"},
    {"title": "Sales Operations Intern", "skills": ["CRM", "Data Entry"], "location": "Irving", "industry": "Business"},
    {"title": "Supply Chain Intern", "skills": ["Logistics", "Data Analysis"], "location": "Plano", "industry": "Business"},
    
    # Medical
    {"title": "Research Assistant", "skills": ["Analytical Skills", "Data Analysis"], "location": "Frisco", "industry": "Medical"},
    {"title": "Clinical Volunteer", "skills": ["Compassion", "Communication"], "location": "Dallas", "industry": "Medical"},
    {"title": "Community Volunteer Coordinator", "skills": ["Organization", "Communication"], "location": "Arlington", "industry": "Medical"},
    {"title": "Public Health Intern", "skills": ["Research", "Data Analysis"], "location": "Plano", "industry": "Medical"},
    {"title": "Nursing Intern", "skills": ["Compassion", "Patient Care"], "location": "Irving", "industry": "Medical"},
    {"title": "Healthcare Administration Intern", "skills": ["Organizational Skills", "Communication"], "location": "Dallas", "industry": "Medical"},
    {"title": "Laboratory Technician Intern", "skills": ["Attention to Detail", "Data Entry"], "location": "Frisco", "industry": "Medical"},
    {"title": "Clinical Research Intern", "skills": ["Data Analysis", "Research"], "location": "Dallas", "industry": "Medical"},
    {"title": "Health Education Intern", "skills": ["Communication", "Teaching"], "location": "Irving", "industry": "Medical"},
    {"title": "Occupational Therapy Intern", "skills": ["Compassion", "Patient Care"], "location": "Plano", "industry": "Medical"},
    {"title": "Physical Therapy Intern", "skills": ["Patient Care", "Compassion"], "location": "Frisco", "industry": "Medical"},
    {"title": "Pharmacy Intern", "skills": ["Medication Management", "Customer Service"], "location": "Dallas", "industry": "Medical"},
    {"title": "Nutritional Science Intern", "skills": ["Research", "Nutrition"], "location": "Irving", "industry": "Medical"},
    {"title": "Health Informatics Intern", "skills": ["IT Skills", "Data Analysis"], "location": "Plano", "industry": "Medical"},
    {"title": "Emergency Room Intern", "skills": ["Compassion", "Communication"], "location": "Frisco", "industry": "Medical"},
    {"title": "Public Health Policy Intern", "skills": ["Research", "Policy Analysis"], "location": "Dallas", "industry": "Medical"},
    {"title": "Veterinary Intern", "skills": ["Compassion", "Animal Care"], "location": "Irving", "industry": "Medical"},
    {"title": "Mental Health Intern", "skills": ["Empathy", "Communication"], "location": "Plano", "industry": "Medical"},
    {"title": "Medical Coding Intern", "skills": ["Attention to Detail", "Data Entry"], "location": "Frisco", "industry": "Medical"},
]

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        layout.bind(size=self.update_background, pos=self.update_background)

        with self.canvas.before:
            Color(0.2, 0.2, 0.8, 1)  # A blueish background
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Welcome Label
        welcome_label = Label(text="Welcome to FutureForger", 
                              font_size=36, 
                              color=(1, 1, 1, 1),  # White text
                              halign='center', 
                              valign='middle')
        welcome_label.bind(size=welcome_label.setter('text_size'))  # For multiline
        layout.add_widget(welcome_label)

        # Subtitle
        subtitle_label = Label(text="Your gateway to internship opportunities", 
                                font_size=24, 
                                color=(0.9, 0.9, 0.9, 1),  # Light gray text
                                halign='center', 
                                valign='middle')
        subtitle_label.bind(size=subtitle_label.setter('text_size'))
        layout.add_widget(subtitle_label)

        # Start Button
        start_button = Button(text="Get Started", 
                              size_hint=(None, None), 
                              size=(200, 50), 
                              pos_hint={'center_x': 0.5}, 
                              background_color=(0, 0.7, 0.3, 1))  # Green button
        start_button.bind(on_press=self.go_to_main)
        layout.add_widget(start_button)

        self.add_widget(layout)

    def update_background(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def go_to_main(self, instance):
        self.manager.current = 'main'


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.bind(size=self.update_background, pos=self.update_background)

        with self.canvas.before:
            Color(0.1, 0.1, 0.5, 1)  # Dark slate blue
            self.rect1 = Rectangle(size=self.size, pos=self.pos)
            Color(1, 1, 1, 1)  # White
            self.rect2 = Rectangle(size=self.size, pos=self.pos)
            Color(0.6, 0.4, 0.8, 1)  # Middle purple
            self.rect3 = Rectangle(size=self.size, pos=self.pos)

        # Title
        title = Label(text="Internship Opportunities", font_size=24, size_hint_y=None, height=40)
        layout.add_widget(title)

        # Industry Selection
        self.industry_spinner = Spinner(
            text='Select Industry',
            values=('Computer Science', 'Business', 'Medical'),
            size_hint=(1, None),
            height=40
        )
        layout.add_widget(self.industry_spinner)

        # Location Selection
        self.location_spinner = Spinner(
            text='Select Location',
            values=('Remote', 'Dallas', 'Frisco', 'Irving', 'Plano', 'Arlington'),
            size_hint=(1, None),
            height=40
        )
        layout.add_widget(self.location_spinner)

        # Skill Buttons
        self.skills_buttons = {}
        skills = ["Python", "Java", "C++", "Communication", "Data Analysis", "Teamwork", "Machine Learning", "Research", "Creativity"]
        skills_layout = GridLayout(cols=3, spacing=10, size_hint_y=None)
        skills_layout.bind(minimum_height=skills_layout.setter('height'))

        for skill in skills:
            button = Button(text=skill, size_hint_y=None, height=40)
            button.bind(on_press=self.toggle_skill)
            skills_layout.add_widget(button)
            self.skills_buttons[skill] = button

        layout.add_widget(skills_layout)

        # Find Opportunities Button
        find_button = Button(text="Find Opportunities", size_hint_y=None, height=50)
        find_button.bind(on_press=self.find_opportunities)
        layout.add_widget(find_button)

        # Profile Button
        profile_button = Button(text="Profile", size_hint_y=None, height=50)
        profile_button.bind(on_press=self.go_to_profile)
        layout.add_widget(profile_button)

        self.output_label = Label(size_hint_y=None, height=200)
        layout.add_widget(self.output_label)

        self.add_widget(layout)

    def update_background(self, *args):
        self.rect1.pos = self.pos
        self.rect1.size = self.size
        self.rect2.pos = self.pos
        self.rect2.size = self.size
        self.rect3.pos = self.pos
        self.rect3.size = self.size

    def toggle_skill(self, button):
        if button.background_color == [1, 1, 1, 1]:  # White
            button.background_color = [0.5, 0.8, 0.5, 1]  # Light Green
        else:
            button.background_color = [1, 1, 1, 1]  # White

    def find_opportunities(self, instance):
        industry = self.industry_spinner.text
        location = self.location_spinner.text
        selected_skills = [skill for skill, button in self.skills_buttons.items() if button.background_color == [0.5, 0.8, 0.5, 1]]

        # Filter internships based on selected criteria
        filtered_internships = [internship for internship in internships if 
                                (internship['industry'] == industry or industry == 'Select Industry') and
                                (internship['location'] == location or location == 'Select Location') and
                                any(skill in internship['skills'] for skill in selected_skills)]

        # Display filtered internships
        if filtered_internships:
            output_text = "Opportunities Found:\n"
            for internship in filtered_internships:
                output_text += f"Title: {internship['title']}\n" \
                               f"Location: {internship['location']}\n" \
                               f"Skills: {', '.join(internship['skills'])}\n\n"
            self.output_label.text = output_text
        else:
            self.output_label.text = "No opportunities found."

    def go_to_profile(self, instance):
        self.manager.current = 'profile'


class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.bind(size=self.update_background, pos=self.update_background)

        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # Light gray background
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Profile Title
        title = Label(text="User Profile", font_size=24, size_hint_y=None, height=40)
        layout.add_widget(title)

        # Name Input
        self.name_input = TextInput(hint_text='Enter your name', size_hint_y=None, height=40)
        layout.add_widget(self.name_input)

        # Resume Link Input
        self.resume_input = TextInput(hint_text='Enter Google Drive link to your resume', size_hint_y=None, height=40)
        layout.add_widget(self.resume_input)

        # Save Profile Button
        save_button = Button(text="Save Profile", size_hint_y=None, height=50)
        save_button.bind(on_press=self.save_profile)
        layout.add_widget(save_button)

        # Back Button
        back_button = Button(text="Back to Main", size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_background(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def save_profile(self, instance):
        profile_info = {
            "Name": self.name_input.text,
            "Resume Link": self.resume_input.text,
        }
        print("Profile Information:", json.dumps(profile_info, indent=2))

    def go_back(self, instance):
        self.manager.current = 'main'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ProfileScreen(name='profile'))
        return sm


if __name__ == '__main__':
    MyApp().run()


