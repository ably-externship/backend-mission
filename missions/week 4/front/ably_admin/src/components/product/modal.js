import "./modal.css";
import { useState, useEffect,useRef } from 'react';
import { Dialog } from '@mui/material';
function Modal({ closeModal }) {
  const el = useRef()


  const handleCloseModal = (e) => {
    if (el.current && !el.current.contains(e.target)) {
      console.log("test")
      closeModal();
    }
  }
  
  useEffect(() => {
    window.addEventListener('click', handleCloseModal);
    return () => {
      window.removeEventListener('click', handleCloseModal)
    };
  }, [])

  return (
    <div className="detail-modal">
      <div>SDfadfasdfk;asdf</div>
      <div className="detail-model-submit">
      </div>
    </div>


  )
}
export default Modal;