import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import Divider from "@material-ui/core/Divider";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
  },
}));

const Results = (props) => {
  const classes = useStyles();
  const { results } = props;

  const displayResults = results.map((result) => {
    return (
      <div key={result.name}>
        <ListItem key={result.name}>
          <ListItemText
            primary={result.name}
            secondary={`${result.distance} km`}
          />
        </ListItem>
        <Divider component="li" />
      </div>
    );
  });

  return <List className={classes.root}>{displayResults}</List>;
};

export default Results;
