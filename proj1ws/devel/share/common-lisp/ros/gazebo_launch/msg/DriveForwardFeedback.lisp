; Auto-generated. Do not edit!


(cl:in-package gazebo_launch-msg)


;//! \htmlinclude DriveForwardFeedback.msg.html

(cl:defclass <DriveForwardFeedback> (roslisp-msg-protocol:ros-message)
  ((progress
    :reader progress
    :initarg :progress
    :type cl:float
    :initform 0.0))
)

(cl:defclass DriveForwardFeedback (<DriveForwardFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DriveForwardFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DriveForwardFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gazebo_launch-msg:<DriveForwardFeedback> is deprecated: use gazebo_launch-msg:DriveForwardFeedback instead.")))

(cl:ensure-generic-function 'progress-val :lambda-list '(m))
(cl:defmethod progress-val ((m <DriveForwardFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gazebo_launch-msg:progress-val is deprecated.  Use gazebo_launch-msg:progress instead.")
  (progress m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DriveForwardFeedback>) ostream)
  "Serializes a message object of type '<DriveForwardFeedback>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'progress))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DriveForwardFeedback>) istream)
  "Deserializes a message object of type '<DriveForwardFeedback>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'progress) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DriveForwardFeedback>)))
  "Returns string type for a message object of type '<DriveForwardFeedback>"
  "gazebo_launch/DriveForwardFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DriveForwardFeedback)))
  "Returns string type for a message object of type 'DriveForwardFeedback"
  "gazebo_launch/DriveForwardFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DriveForwardFeedback>)))
  "Returns md5sum for a message object of type '<DriveForwardFeedback>"
  "70805092fd20e110765c7b79e8efb737")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DriveForwardFeedback)))
  "Returns md5sum for a message object of type 'DriveForwardFeedback"
  "70805092fd20e110765c7b79e8efb737")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DriveForwardFeedback>)))
  "Returns full string definition for message of type '<DriveForwardFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%float32 progress~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DriveForwardFeedback)))
  "Returns full string definition for message of type 'DriveForwardFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%float32 progress~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DriveForwardFeedback>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DriveForwardFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'DriveForwardFeedback
    (cl:cons ':progress (progress msg))
))
