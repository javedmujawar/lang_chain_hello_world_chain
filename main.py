import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()
def main():
    """Print a simple hello message."""
    print("Hello from langchain-source")
    information = """Gopalaswamy Doraiswamy Naidu (23 March 1893 – 4 January 1974) was an Indian innovator, inventor, industrialist, and educator. He redesigned and transformed imported technologies into practical and affordable innovations for India, and is widely regarded as a versatile genius. His contributions spanned industrial, electrical, mechanical, agricultural, and automobile engineering. Credited with several innovations, he manufactured India's first indigenous electric motor and petrol engine car. He established several companies and educational institutions. Gopalaswamy Doraiswamy Naidu was born on 23 March 1893 in a Telugu-speaking agrarian family at Kalangal in Coimbatore district of the erstwhile Madras Presidency. His mother died when he was a few months old. He disliked school and dropped out in the third grade.[3][4][5] He worked in his father's farm during the day, and taught himself in the evenings.[5]


    The first motorcycle purchased by Naidu
    As a teenager, Naidu came across a Rudge-Whitworth motorcycle for the first time when a British official drove one to his village. This sparked his curiosity, and ignited a fascination with mechanics.[3][4] He later moved to Coimbatore, where he worked several jobs, including waiter, mechanic, and cotton mill worker. He saved about ₹400 (equivalent to ₹100,000 or US$1,100 in 2023) over three years to purchase the same motorcycle, which he had seen a few years back in his village. He then took apart and put back together to understand how it worked.[3][5]

    In 1915, Naidu joined a restaurant run by the British businessman Robert Stanes, where he learned English.[5] He later worked in a ginning factory, and traveled to Bombay to capitalize on the cotton textile industry boom; however, he lost his savings when prices subsequently dropped.[6]

    Career
    In 1920, Naidu offered to work as a mechanic for Stanes, who helped him secure a loan of ₹4,000 (equivalent to ₹730,000 or US$7,600 in 2023) to start his own transport business, and sold one of his buses to him in 1921. Naidu personally drove the bus for his transport service between Palani and Pollachi. He later established the transport company, United Motor Service, which operated a fleet of 280 buses by 1933, and 600 buses in the late 1930s.[4][5][6]


    India's first indigenous electric motor developed by G. D. Naidu
    Naidu founded New Electric Works in 1930.[4] In the mid-1930s, he developed the "Rasant" electric shaver by adapting the motor of a toy car.[3][5] After patenting the device in Europe, he began large scale manufacturing by importing components from several European countries. The product achieved commercial success, selling in several European countries, and was featured in American magazine advertisements.[5] Working along with D. Balasundaram, Naidu developed India's first indigenous electric motor in 1937, which led to establishment of Textool and Lakshmi Machine Works.[3] Initially, they manufactured castings and windings, while importing bearings and enamelled wire for the motors. However, due to the disruption of the supply chain due to the Second World War, they built machines to manufacture the wires and bearings locally.[7]

    During the Second World War, Naidu manufactured electronic components including capacitors and resistors in Coimbatore, which he supplied to the British Army.[5] He later built several products such as voting machines, juice extractors, coin-operated phonographs, electronic calculators, lathes, projectors, five-valve radios, vending machines, kerosene-run fans, and a distance adjuster for film cameras.[5][4][6] In 1952, Naidu built two-seater petrol engine car costing ₹2,000 (equivalent to ₹220,000 or US$2,200 in 2023). However, the government denied him license to produce these cars.[8] He established several companies including Universal Radiators, Gopal Clock Industry, Coimbatore Diesel Products and Coimbatore Engineering, Coimbatore Armature Winding Works, and UMS Radio Company.[4]

    Later life and death

    G D Science Museum in Coimbatore
    In 1944, Naidu retired from active involvement with his companies.[4] He had established a 40 acres (16 ha) farm in 1941, in which he researched and identified new varieties of cotton, maize, and papaya.[4][9] He was involved in various philanthropic activities, and established grants for research and welfare schemes.[4] He founded the Industrial Labour Welfare Association to impart vocational training and donated land for the Indian Chamber of Commerce and Industry.[9] He researched and devised methods to build low cost dwellings, that could be built within a day.[5][9]

    In 1945, Naidu established India's first polytechnic college in Coimbatore, and served as its first principal.[4][9] He worked with C. S. Ratnasabhapathy Mudaliar and R. K. Shanmukham Chetty to bring the waters of Siruvani River to Coimbatore.[10] In 1950, he established the G D Science Museum in Coimbatore. He also organized temporary exhibitions of various machines and gadgets across various cities to demonstrate how they worked.[11] It became permanent as the G. D. Naidu Industrial Exhibition in Coimbatore in 1967.[12]

    Naidu was an avid photographer, and traveled to several countries.[5][13] He traveled to the funeral of King George V in London,[4] and met Adolf Hitler in Germany.[14] He died on 4 January 1974.[5][4]

    Legacy
    Naidu is widely considered a versatile genius, and known by the epithet, "Edison of India".[1][2] C. V. Raman said of Naidu: "A great educator, an entrepreneur in many fields of engineering and industry, a warm-hearted man filled with love for his fellows and a desire to help them in their troubles, Mr Naidu is truly a man in a million – perhaps this is an understatement!"[4] He is credited as one of the "wealth creators" of Coimbatore.[15]

    Several institutions and places including the GD Matriculation Higher Secondary School,[16] and the G. D. Naidu Elevated Expressway, are named after him.[17] Makkal Sinthanai Peravai, a non-profit organization, awards the annual G. D. Naidu Award for Young Scientist in his honour.[18]

    Gedee Car Museum
    Gedee Car Museum is a private vintage car museum founded by G. D. Gopal in 2015 as a commemoration of his father, G. D. Naidu."""

    summery_template = """
    given the information {information} about a person I want you to create:
    1. A sotry summerny
    2.two interesting facts about the
    3. one question about them
    """

    summery_prompt_template = PromptTemplate(
        input_variables=["information"], template=summery_template
    )
    llm = ChatOllama(temperature=0, model="gemma3:270m")

    chain = summery_prompt_template | llm
    response = chain.invoke(input={"information":information})
    print(response)


if __name__ == "__main__":
    print("... Started ...")
    main()
