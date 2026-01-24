from LLDInterviewQuestions.Design_parking_lot.exceptions import TicketNotClosedException
from LLDInterviewQuestions.Design_parking_lot.models.ticket import Ticket
from LLDInterviewQuestions.Design_parking_lot.strategies.pricing_stratergy import PricingStrategy


class HourlyPricing(PricingStrategy):
    def __init__(self, rate_per_hour: float = 50.0, minimum_hours: int = 1):
        """
        Initialize hourly pricing strategy.
        
        Args:
            rate_per_hour: Rate per hour in currency units
            minimum_hours: Minimum hours to charge (default 1)
        """
        self.rate_per_hour = rate_per_hour
        self.minimum_hours = minimum_hours

    def calculate(self, ticket: Ticket) -> float:
        if ticket.exit_time is None:
            raise TicketNotClosedException(ticket.ticket_id)

        duration = ticket.exit_time - ticket.entry_time
        total_seconds = duration.total_seconds()
        hours = total_seconds / 3600
        
        # Round up to nearest hour, but minimum is minimum_hours
        billable_hours = max(self.minimum_hours, int(hours) + (1 if hours % 1 > 0 else 0))
        
        return billable_hours * self.rate_per_hour
