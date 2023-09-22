; Auto-generated. Do not edit!


(cl:in-package custom_behavior_actions-msg)


;//! \htmlinclude DriveForward.msg.html

(cl:defclass <DriveForward> (roslisp-msg-protocol:ros-message)
  ((distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass DriveForward (<DriveForward>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DriveForward>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DriveForward)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_behavior_actions-msg:<DriveForward> is deprecated: use custom_behavior_actions-msg:DriveForward instead.")))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <DriveForward>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_behavior_actions-msg:distance-val is deprecated.  Use custom_behavior_actions-msg:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DriveForward>) ostream)
  "Serializes a message object of type '<DriveForward>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DriveForward>) istream)
  "Deserializes a message object of type '<DriveForward>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DriveForward>)))
  "Returns string type for a message object of type '<DriveForward>"
  "custom_behavior_actions/DriveForward")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DriveForward)))
  "Returns string type for a message object of type 'DriveForward"
  "custom_behavior_actions/DriveForward")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DriveForward>)))
  "Returns md5sum for a message object of type '<DriveForward>"
  "6e77fb10f0c8b4833ec273aa9ac74459")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DriveForward)))
  "Returns md5sum for a message object of type 'DriveForward"
  "6e77fb10f0c8b4833ec273aa9ac74459")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DriveForward>)))
  "Returns full string definition for message of type '<DriveForward>"
  (cl:format cl:nil "# Custom message for driving forward~%float32 distance    # Distance to drive forward (in meters)~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DriveForward)))
  "Returns full string definition for message of type 'DriveForward"
  (cl:format cl:nil "# Custom message for driving forward~%float32 distance    # Distance to drive forward (in meters)~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DriveForward>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DriveForward>))
  "Converts a ROS message object to a list"
  (cl:list 'DriveForward
    (cl:cons ':distance (distance msg))
))
