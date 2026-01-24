"""
Pricing strategy that applies different rates during peak hours.
"""

import datetime

from LLDInterviewQuestions.Design_parking_lot.exceptions import TicketNotClosedException
from LLDInterviewQuestions.Design_parking_lot.models.ticket import Ticket
from LLDInterviewQuestions.Design_parking_lot.strategies.pricing_stratergy import PricingStrategy


class PeakHourPricing(PricingStrategy):
    """
    Pricing strategy with different rates for peak and off-peak hours.
    """
    
    def __init__(
        self, 
        peak_rate_per_hour: float = 75.0,
        off_peak_rate_per_hour: float = 50.0,
        peak_start_hour: int = 9,  # 9 AM
        peak_end_hour: int = 18,   # 6 PM
        minimum_hours: int = 1
    ):
        """
        Initialize peak hour pricing strategy.
        
        Args:
            peak_rate_per_hour: Rate during peak hours
            off_peak_rate_per_hour: Rate during off-peak hours
            peak_start_hour: Start of peak hours (0-23)
            peak_end_hour: End of peak hours (0-23)
            minimum_hours: Minimum hours to charge
        """
        self.peak_rate_per_hour = peak_rate_per_hour
        self.off_peak_rate_per_hour = off_peak_rate_per_hour
        self.peak_start_hour = peak_start_hour
        self.peak_end_hour = peak_end_hour
        self.minimum_hours = minimum_hours
    
    def _is_peak_hour(self, dt: datetime.datetime) -> bool:
        """Check if given datetime is during peak hours."""
        hour = dt.hour
        if self.peak_start_hour <= self.peak_end_hour:
            return self.peak_start_hour <= hour < self.peak_end_hour
        else:
            # Peak hours span midnight (e.g., 22:00 to 6:00)
            return hour >= self.peak_start_hour or hour < self.peak_end_hour
    
    def calculate(self, ticket: Ticket) -> float:
        if ticket.exit_time is None:
            raise TicketNotClosedException(ticket.ticket_id)
        
        duration = ticket.exit_time - ticket.entry_time
        total_seconds = duration.total_seconds()
        total_hours = total_seconds / 3600
        
        # Calculate billable hours (round up)
        billable_hours = max(self.minimum_hours, int(total_hours) + (1 if total_hours % 1 > 0 else 0))
        
        # Calculate cost hour by hour
        total_cost = 0.0
        current_time = ticket.entry_time
        
        for hour in range(billable_hours):
            if self._is_peak_hour(current_time):
                total_cost += self.peak_rate_per_hour
            else:
                total_cost += self.off_peak_rate_per_hour
            
            # Move to next hour
            current_time += datetime.timedelta(hours=1)
        
        return total_cost
