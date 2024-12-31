import React, { useState, useEffect } from 'react';
import axios from 'axios';

const BookingSummary = () => {
  const [summary, setSummary] = useState([]);

  useEffect(() => {
    fetchSummary();
  }, []);

  const fetchSummary = () => {
    axios.get('http://localhost:5000/api/tickets/summary')
      .then(response => setSummary(response.data))
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>Booking Summary</h2>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Show ID</th>
            <th>Event Name</th>
            <th>Start Time</th>
            <th>End Time</th>
            <th>Total Tickets Booked</th>
          </tr>
        </thead>
        <tbody>
          {summary.map(show => (
            <tr key={show.show_id}>
              <td>{show.show_id}</td>
              <td>{show.event_name}</td>
              <td>{new Date(show.start_time).toLocaleString()}</td>
              <td>{new Date(show.end_time).toLocaleString()}</td>
              <td>{show.total_tickets || 0}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default BookingSummary;
