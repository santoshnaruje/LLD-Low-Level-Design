from LLDInterviewQuestions.Design_parking_lot.models.ticket import Ticket


class PricingStrategy:
    def calculate(self, ticket: Ticket) -> float:
        raise NotImplementedError
