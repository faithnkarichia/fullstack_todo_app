import { useState } from 'react'

import './App.css'
import Todos from './pages/todos'
  
import Login from './pages/login_page'
import { BrowserRouter as Router, Routes, Route, Outlet, Navigate } from "react-router-dom";


function App() {
 

  return (
  
      <Routes>
    <Route path="/login" element={<Login/>}/>
    <Route path="/todos" element={<Todos/>}/>
   </Routes>
    
   
  )
}

export default App
