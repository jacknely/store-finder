import React from "react";
import { TextField } from "@material-ui/core";

const MyField = (props) => {
  const { values, errors, handleChange, name } = props;
  return (
    <div className="field">
      <TextField
        fullWidth
        name={name}
        id={name}
        value={values[name]}
        type="text"
        label={name.charAt(0).toUpperCase() + name.slice(1)}
        helperText={errors[name]}
        onChange={(e) => {
          handleChange(e);
        }}
      />
    </div>
  );
};

export default MyField;
