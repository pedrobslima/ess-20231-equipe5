const Comment = ({
    user,
    text
    }) => {
        return (
            <div>
              <div>
              <label className="CommUser">{user} </label>
              </div>
              <label className="CommText">{text} </label>
            </div>
      );
  };
  export default Comment;