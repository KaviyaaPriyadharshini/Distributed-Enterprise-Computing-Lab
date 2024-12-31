import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ShowManagement = () => {
  const [shows, setShows] = useState([]);
  const [events, setEvents] = useState([]);
  const [form, setForm] = useState({ start_time: '', end_time: '', stage_event_id: '' });

  useEffect(() => {
    fetchShows();
    fetchEvents();
  }, []);

  const fetchShows = () => {
    axios.get('http://localhost:5000/api/shows')
      .then(response => setShows(response.data))
      .catch(err => console.error(err));
  };

  const fetchEvents = () => {
    axios.get('http://localhost:5000/api/events')
      .then(response => setEvents(response.data))
      .catch(err => console.error(err));
  };

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    axios.post('http://localhost:5000/api/shows', form)
      .then(() => {
        fetchShows();
        setForm({ start_time: '', end_time: '', stage_event_id: '' });
      })
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>Show Management</h2>
      <form onSubmit={handleSubmit}>
        <label>Start Time:</label>
        <input
          type="datetime-local"
          name="start_time"
          value={form.start_time}
          onChange={handleChange}
          required
        />
        <br /><br />
        <label>End Time:</label>
        <input
          type="datetime-local"
          name="end_time"
          value={form.end_time}
          onChange={handleChange}
          required
        />
        <br /><br />
        <label>Event:</label>
        <select name="stage_event_id" value={form.stage_event_id} onChange={handleChange} required>
          <option value="">Select Event</option>
          {events.map(event => (
            <option key={event.id} value={event.id}>{event.name}</option>
          ))}
        </select>
        <br /><br />
        <button type="submit">Add Show</button>
      </form>
      <h3>Existing Shows</h3>
      <ul>
        {shows.map(show => (
          <li key={show.id}>
            <strong>{show.event_name}</strong>: {new Date(show.start_time).toLocaleString()} - {new Date(show.end_time).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ShowManagement;
