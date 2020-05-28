import React from "react";
import { render, fireEvent, waitForElement } from "@testing-library/react";
import "@testing-library/jest-dom/extend-expect";
import App from "./App";
import axiosMock from "axios";

jest.mock("axios");

test("on calling char_count it renders the number of characters", async () => {
  const testString = "React Testing";
  const url = `/char_count?text=${testString}`;
  axiosMock.get.mockResolvedValueOnce({
    data: { count: testString.length },
  });
  const { getByText, getByPlaceholderText, getByTestId } = render(<App />);

  const charInputElement = getByPlaceholderText("my string");
  expect(charInputElement).toBeInTheDocument();

  fireEvent.change(charInputElement, { target: { value: testString } });
  fireEvent.click(getByText("have?"));
  const responseTextNode = await waitForElement(() =>
    getByTestId("char-count")
  );

  expect(axiosMock.get).toHaveBeenCalledTimes(1);
  expect(axiosMock.get).toHaveBeenCalledWith(url);
  expect(getByTestId("char-count")).toHaveTextContent(
    `${testString.length} characters!`
  );
});
