import pandas as pd

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExtractFoodEntity(Action):

    def name(self) -> Text:
        return "action_extract_food_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_entity = next(tracker.get_latest_entity_values('food'), None)

        if food_entity:
            dispatcher.utter_message(text=f"You have selected {food_entity} as your food choice")
        else:
            dispatcher.utter_message(text="I am sorry, I could not detect the food choice")

            return []


class OrderFoodAction(Action):

    def name(self) -> Text:
        return "action_order_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure, which kind of food would you like to order")

        return []


class ConfirmOrderAction(Action):

    def name(self) -> Text:
        return "action_confirm_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food_entity = next(tracker.get_latest_entity_values('food'), None)

        if food_entity:
            dispatcher.utter_message(text=f"You have selected {food_entity} as your food choice")
        else:
            dispatcher.utter_message(text="I am sorry, I could not detect the food choice")

            return []


class InfoDiseaseAction(Action):

    def name(self) -> Text:
        return "confirm_information_diseases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure, what disease would you need an information of?")

        return []

class ProvideInformationDiseases(Action):

    def name(self) -> Text:
        return "action_information_diseases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        try:
            # Load the CSV file containing disease information
            df = pd.read_csv('./dataset/healthdata.csv')
            print("CSV file loaded successfully")
        except FileNotFoundError:
            dispatcher.utter_message(text="The dataset file was not found.")
            return []
        except pd.errors.EmptyDataError:
            dispatcher.utter_message(text="The dataset file is empty.")
            return []
        except pd.errors.ParserError:
            dispatcher.utter_message(text="The dataset file is corrupted.")
            return []

            # Get the latest entity value for 'disease'
        disease_entity = next(tracker.get_latest_entity_values('disease'), None)
        print(f"Disease entity: {disease_entity}")

        # Check if the disease entity exists and find the corresponding information
        if disease_entity:
            # Assuming the CSV has columns named 'disease' and 'information'
            information_row = df[df['disease'].str.lower() == disease_entity.lower()]
            print(f"Information row: {information_row}")

            if not information_row.empty:
                # Select the first matching information (assuming each disease has only one information entry)
                information_text = information_row.iloc[0]['information']
                dispatcher.utter_message(text=information_text)
            else:
                dispatcher.utter_message(text="I couldn't find specific information for that disease.")
        else:
            dispatcher.utter_message(text="Please specify a disease.")

        return []


class RecommendationDiseaseAction(Action):

    def name(self) -> Text:
        return "confirm_recommendation_diseases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure, what disease would you need a recommendation of?")

        return []

class ProvideRecommendationDiseases(Action):

    def name(self) -> Text:
        return "action_recommendation_diseases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Load the CSV file containing disease recommendations
        df = pd.read_csv('./dataset/healthdata.csv')

        # Get the latest entity value for 'disease'
        disease_entity = next(tracker.get_latest_entity_values('disease'), None)

        # Check if the disease entity exists and find the corresponding recommendation
        if disease_entity:
            # Assuming the CSV has columns named 'disease' and 'recommendation'
            recommendation_row = df[df['disease'] == disease_entity]

            if not recommendation_row.empty:
                # Select the first matching recommendation (assuming each disease has only one recommendation)
                recommendation_text = recommendation_row.iloc[0]['recommendation']
                dispatcher.utter_message(text=recommendation_text)
            else:
                dispatcher.utter_message(text="I couldn't find a specific recommendation for that disease.")
        else:
            dispatcher.utter_message(text="Please specify a disease.")

        return []


class MedicineDiseaseAction(Action):

    def name(self) -> Text:
        return "confirm_medicine_diseases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure, what disease would you need a medicine of?")

        return []


class ProvideMedicineDiseases(Action):

    def name(self) -> Text:
        return "action_medicine_diseases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Load the CSV file containing disease recommendations
        df = pd.read_csv('./dataset/healthdata.csv')

        # Get the latest entity value for 'disease'
        disease_entity = next(tracker.get_latest_entity_values('disease'), None)

        # Check if the disease entity exists and find the corresponding recommendation
        if disease_entity:
            # Assuming the CSV has columns named 'disease' and 'recommendation'
            medicine_row = df[df['disease'] == disease_entity]

            if not medicine_row.empty:
                # Select the first matching recommendation (assuming each disease has only one recommendation)
                medicine_text = medicine_row.iloc[0]['medicine']
                dispatcher.utter_message(text=medicine_text)
            else:
                dispatcher.utter_message(text="I couldn't find a specific medicine for that disease.")
        else:
            dispatcher.utter_message(text="Please specify a disease.")

        return []


class SymptomDiseaseAction(Action):

    def name(self) -> Text:
        return "confirm_symptom_diseases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sure, what disease would you need a symptoms information of?")

        return []

class ProvideSymptomsDiseases(Action):

    def name(self) -> Text:
        return "action_symptom_diseases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Load the CSV file containing disease recommendations
        df = pd.read_csv('./dataset/healthdata.csv')

        # Get the latest entity value for 'disease'
        disease_entity = next(tracker.get_latest_entity_values('disease'), None)

        # Check if the disease entity exists and find the corresponding recommendation
        if disease_entity:
            # Assuming the CSV has columns named 'disease' and 'recommendation'
            symptom_row = df[df['disease'] == disease_entity]

            if not symptom_row.empty:
                # Select the first matching recommendation (assuming each disease has only one recommendation)
                symptom_text = symptom_row.iloc[0]['symptom']
                dispatcher.utter_message(text=symptom_text)
            else:
                dispatcher.utter_message(text="I couldn't find a specific symptom for that disease.")
        else:
            dispatcher.utter_message(text="Please specify a disease.")

        return []