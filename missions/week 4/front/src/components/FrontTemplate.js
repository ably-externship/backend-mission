import React from 'react';
import styled from 'styled-components';

const FrontTemplateBlock = styled.div`
  width: 90%;
  height: 70%;

  position: relative;
  background-color: white;
  border-radius: 16px;
  box-shadow: 0 0 8px 0 rgba(0, 0, 0, 0.04);

  margin: 50px auto;
  padding: 20px 0;
  display: flex;
  flex-direction: column;

  font-family: "Gowun Dodum";

  h2 {
    text-align: center;
  }
`;

function FrontTemplate({ children }) {
  return <FrontTemplateBlock>{children}</FrontTemplateBlock>;
}

export default FrontTemplate;