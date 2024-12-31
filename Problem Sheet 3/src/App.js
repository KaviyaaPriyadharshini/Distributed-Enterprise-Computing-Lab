import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import EventManagement from './components/EventManagement';
import ShowManagement from './components/ShowManagement';
import TicketBooking from './components/TicketBooking';
import BookingSummary from './components/BookingSummary';

function App() {
  return (
    <Router>
      <div style={{ padding: '20px' }}>
        <h1>Stage Events Management</h1>
        <nav>
          <Link to="/events" style={{ marginRight: '10px' }}>Events</Link>
          <Link to="/shows" style={{ marginRight: '10px' }}>Shows</Link>
          <Link to="/book-tickets" style={{ marginRight: '10px' }}>Book Tickets</Link>
          <Link to="/summary">Booking Summary</Link>
        </nav>
        <hr />
        <Routes>
          <Route path="/events" element={<EventManagement />} />
          <Route path="/shows" element={<ShowManagement />} />
          <Route path="/book-tickets" element={<TicketBooking />} />
          <Route path="/summary" element={<BookingSummary />} />
          <Route path="/" element={<EventManagement />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
