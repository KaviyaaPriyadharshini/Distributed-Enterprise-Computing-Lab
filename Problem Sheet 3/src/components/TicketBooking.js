import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TicketBooking = () => {
  const [shows, setShows] = useState([]);
  const [form, setForm] = useState({ price: '', customer: '', no_of_seats: '', stage_event_show_id: '' });

  useEffect(() => {
    fetchShows();
  }, []);

  const fetchShows = () => {
    axios.get('http://localhost:5000/api/shows')
      .then(response => setShows(response.data))
      .catch(err => console.error(err));
  };

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('http://localhost:5000/api/tickets', form)
      .then(() => {
        alert('Tickets booked successfully!');
        setForm({ price: '', customer: '', no_of_seats: '', stage_event_show_id: '' });
      })
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>Book Tickets</h2>
      <form onSubmit={handleSubmit}>
        <label>Price:</label>
        <input
          type="number"
          name="price"
          value={form.price}
          onChange={handleChange}
          required
        />
        <br /><br />
        <label>Customer Name:</label>
        <input
          type="text"
          name="customer"
          value={form.customer}
          onChange={handleChange}
          required
        />
        <br /><br />
        <label>Number of Seats:</label>
        <input
          type="number"
          name="no_of_seats"
          value={form.no_of_seats}
          onChange={handleChange}
          required
        />
        <br /><br />
        <label>Show:</label>
        <select name="stage_event_show_id" value={form.stage_event_show_id} onChange={handleChange} required>
          <option value="">Select Show</option>
          {shows.map(show => (
            <option key={show.id} value={show.id}>
              {show.event_name} - {new Date(show.start_time).toLocaleString()}
            </option>
          ))}
        </select>
        <br /><br />
        <button type="submit">Book Tickets</button>
      </form>
    </div>
  );
};

export default TicketBooking;
