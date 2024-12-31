import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EventManagement = () => {
  const [events, setEvents] = useState([]);
  const [form, setForm] = useState({ name: '', detail: '', organizer: '' });

  useEffect(() => {
    fetchEvents();
  }, []);

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
    axios.post('http://localhost:5000/api/events', form)
      .then(() => {
        fetchEvents();
        setForm({ name: '', detail: '', organizer: '' });
      })
      .catch(err => console.error(err));
  };

  const handleDelete = id => {
    axios.delete(`http://localhost:5000/api/events/${id}`)
      .then(() => fetchEvents())
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h2>Event Management</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Event Name"
          value={form.name}
          onChange={handleChange}
          required
        />
        <br /><br />
        <input
          type="text"
          name="detail"
          placeholder="Event Detail"
          value={form.detail}
          onChange={handleChange}
        />
        <br /><br />
        <input
          type="text"
          name="organizer"
          placeholder="Organizer"
          value={form.organizer}
          onChange={handleChange}
        />
        <br /><br />
        <button type="submit">Add Event</button>
      </form>
      <h3>Existing Events</h3>
      <ul>
        {events.map(event => (
          <li key={event.id}>
            <strong>{event.name}</strong> - {event.detail} (Organizer: {event.organizer})
            <button onClick={() => handleDelete(event.id)} style={{ marginLeft: '10px' }}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EventManagement;
