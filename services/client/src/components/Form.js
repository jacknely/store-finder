import React from "react";
import { Formik } from "formik";
import * as Yup from "yup";
import "./Form.css";
import MyField from "./MyField";

const MyForm = (props) => {
  return (
    <div className="form-cont">
      <Formik
        initialValues={{
          radius: "",
          postcode: "",
        }}
        onSubmit={(values, { setSubmitting }) => {
          props.handleLoginFormSubmit(values);
          setSubmitting(false);
        }}
        validationSchema={Yup.object().shape({
          radius: Yup.number()
            .transform((value) => (isNaN(value) ? undefined : value))
            .required("Insert radius in km"),
          postcode: Yup.string().required("Required"),
        })}
      >
        {(props) => {
          const { values, errors, handleChange, handleSubmit } = props;
          return (
            <form onSubmit={handleSubmit}>
              <MyField
                name="postcode"
                values={values}
                errors={errors}
                handleChange={handleChange}
              />
              <MyField
                name="radius"
                values={values}
                errors={errors}
                handleChange={handleChange}
              />
              <button className="button" type="submit">
                Submit
              </button>
            </form>
          );
        }}
      </Formik>
      <div className="results"></div>
    </div>
  );
};

export default MyForm;
